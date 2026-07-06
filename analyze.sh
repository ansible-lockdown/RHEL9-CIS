#!/bin/bash

# Get all notified handlers (excluding YAML anchors)
notified=$(grep -rh "notify:" tasks/ --include="*.yml" | \
    grep -v "&mount_option_notify" | grep -v "\*mount_option_notify" | \
    sed 's/.*notify: *//;s/^[[:space:]]*- *//' | \
    sed 's/{{.*//g' | \
    grep -v "^$" | sort -u)

# Get all listen targets (callable handler names)
listen=$(grep "^  listen:" handlers/main.yml | sed 's/.*listen: "//' | sed 's/"$//' | sort -u)

# Get all handler names (task names that don't have listen)
handler_names=$(grep "^- name:" handlers/main.yml | sed 's/.*name: "//' | sed 's/"$//' | sort -u)

echo "=== HANDLERS NOTIFIED FROM TASKS ==="
echo "$notified"

echo ""
echo "=== LISTEN TARGETS (handlers accessible via notify) ==="
echo "$listen"

echo ""
echo "=== HANDLER TASK NAMES (not via listen) ==="
echo "$handler_names"

echo ""
echo "=== CROSS-REFERENCE: Notified but no listen target ==="
comm -23 <(echo "$notified") <(echo "$listen")

echo ""
echo "=== CROSS-REFERENCE: Listen target exists, but notified with different case/name ==="
# Check for case-sensitive mismatches
for notify in $(echo "$notified"); do
  if ! grep -q "^  listen: \"$notify\"" handlers/main.yml; then
    echo "  [MISMATCH] '$notify' (notified) does not match any listen: target"
  fi
done

echo ""
echo "=== HANDLERS NOT REFERENCED (defined but never notified) ==="
# Check which listen targets are never referenced
for listen_target in $(echo "$listen"); do
  if ! echo "$notified" | grep -q "^${listen_target}$"; then
    echo "  $listen_target"
  fi
done

# Also check handler names (direct task names, not listen targets)
echo ""
echo "=== HANDLER TASK NAMES NOT VIA LISTEN THAT ARE NEVER NOTIFIED ==="
for handler_name in $(echo "$handler_names"); do
  # Skip those that have listen targets
  if ! grep -q "^- name: \"$handler_name\"" handlers/main.yml -A 20 | grep "^  listen:"; then
    if ! echo "$notified" | grep -q "^${handler_name}$"; then
      # Check if this handler has a listen target at all
      if grep -q "^- name: \"$handler_name\"" handlers/main.yml -A 20 | grep "^  listen:"; then
        continue  # Skip if has listen
      fi
      echo "  $handler_name"
    fi
  fi
done
