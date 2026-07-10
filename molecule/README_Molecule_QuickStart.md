# Molecule Quick Start - RHEL9-CIS

> Audience: anyone new to molecule testing with this Ansible Lockdown role. Read top-to-bottom the first time; come back to the reference tables later.

## Two scenarios live here: `default/` vs `ubi/`

This `molecule/` directory ships two scenarios. Pick the right one before running:

| | `molecule/default/` (canonical) | `molecule/ubi/` (smoke test) |
|---|---|---|
| **When to use** | Every QA cycle, before merging/pushing. This is the **gating scenario**. | Occasional sanity check against Red Hat's upstream UBI image (e.g. confirm role still applies on the registry image, not just on the Rocky variant). |
| **Container image** | `rockylinux/rockylinux:9-ubi-init` | `redhat/ubi9-init:latest` |
| **Container name** | `rhel9-cis-qa` | `rhel9-cis-ubi` |
| **Audit branch** | `benchmark_v2.0.0` (from `vars/audit.yml` via `benchmark_version` in `defaults/main.yml`) | same as `default/` |
| **`rhel9cis_disruption_high`** | `true` (exercises full code path) | `false` (conservative) |
| **`fetch_audit_output`** | `true` (auto-copies audit JSONs out to `_temp_fetched_audits/`) | not set (audit results stay inside the container; `docker cp` them out manually) |
| **`prepare.yml` package set** | Full (audit, aide, chrony, rsyslog, logrotate, cronie, acl, kmod, dnf-plugins-core, python3-libselinux, python3-policycoreutils, python3-dnf-plugin-versionlock, tmux, git, procps-ng) | Subset; some packages aren't in UBI repos so installs run with `ignore_errors: true` |
| **Maintenance** | Kept in lock-step with the role and audit repos every cycle | Updated less often; intentionally drift-tolerant |

**Rule of thumb:** if you don't know which to use, use `default/`. `ubi/` is for cases where you specifically want to validate against Red Hat's `redhat/ubi9-init` registry image rather than the Rocky variant.

The rest of this document focuses on the `default/` scenario. To run the `ubi/` scenario instead, swap `molecule destroy` -> `molecule -s ubi destroy` (and the same `-s ubi` flag on `converge`, `verify`).

## What this scenario does

Molecule spins up a throwaway Rocky 9 Docker container, applies the **whole** Ansible Lockdown RHEL 9 CIS role against it, then runs the paired goss audit (from the `RHEL9-CIS-Audit` repo) to see how many controls passed and how many still fail. It's the gating test you run before merging or pushing benchmark changes.

End-to-end you get:
1. A clean container booted into systemd.
2. Pre-remediation audit (baseline): records which controls are already failing before the role runs.
3. Role converge #1: applies all the CIS remediations.
4. Role converge #2: re-runs to confirm idempotency (zero changed tasks the second time).
5. Post-remediation audit: records the after-picture.
6. Pre and post audit JSON summaries automatically copied out to a directory beside the role for review.

If steps 3 and 4 both report `failed=0` and step 6 shows the post-audit failure count substantially lower than the pre-audit count, the role is shippable.

## Prerequisites

| Need | Why | How to check |
|---|---|---|
| Docker (Desktop or Engine), running | Molecule uses Docker to create the test container | `docker info` returns without error |
| Python 3.10+ | Ansible / Molecule are Python tools | `python3 --version` |
| Ansible venv with `ansible-core >= 2.19`, `molecule`, `molecule-plugins[docker]`, `docker`, `passlib` | Runtime deps for the test | `pip list \| grep -E 'ansible\|molecule'` |
| `git` on the controller | Audit content is cloned from `RHEL9-CIS-Audit` | `git --version` |
| Local clones of **both** `Private-RHEL9-CIS` AND `RHEL9-CIS-Audit` (or network access so the audit repo can be cloned at runtime) | The role pulls audit goss content from the audit repo during converge | `git -C <path-to>/RHEL9-CIS-Audit status` |

One-time venv setup (skip if you already have one):

```bash
python3 -m venv <path-to-your-ansible-venv>
source <path-to-your-ansible-venv>/bin/activate
pip install 'ansible-core>=2.19' 'molecule>=24' 'molecule-plugins[docker]' docker passlib
```

## Quick start

```bash
# Every time
source <path-to-your-ansible-venv>/bin/activate
cd <path-to>/Private-RHEL9-CIS

# Full gating pair
molecule destroy && molecule converge && molecule converge && molecule verify

# QA against an unpublished RHEL9-CIS-Audit branch (see "Overriding the audit branch" below)
molecule destroy && molecule converge -- --extra-vars 'audit_git_version=<your-qa-branch>' && molecule converge && molecule verify
```

The whole sequence takes 15-25 minutes on a modern laptop. Network is needed (clone of audit content + dnf installs) for the first run; subsequent runs reuse the cached Docker image.

## What each command does

| Command | What happens |
|---|---|
| `molecule destroy` | Removes any leftover container from a previous run. Safe to run on a clean system. |
| `molecule converge` (first) | (a) pulls / starts the `rockylinux/rockylinux:9-ubi-init` container, (b) runs `prepare.yml` to install supporting packages, (c) clones the audit content from `RHEL9-CIS-Audit`, (d) runs the pre-remediation audit, (e) applies the full role, (f) runs the post-remediation audit, (g) fetches both audit JSONs to your local `_temp_fetched_audits/` folder. |
| `molecule converge` (second) | Re-runs the role against the already-remediated container. The Ansible `PLAY RECAP` should show `changed=0` (or a small handful of acceptable re-renders) - that's the **idempotency check**. |
| `molecule verify` | Final assertions defined in the scenario (light by default for this role; the real validation is in the audit JSONs). |

## Where the audit results land

After `molecule converge` completes, look at:

```
<working-tree>/_temp_fetched_audits/
  rhel9-cis-qa-RHEL9-CIS-v<ver>_pre_scan_<timestamp>.json
  rhel9-cis-qa-RHEL9-CIS-v<ver>_post_scan_<timestamp>.json
```

The JSONs are goss output - each has a `results: []` array where every entry has a `successful: true|false` field. Compare pre vs. post:

```bash
# How many controls passed before remediation?
jq '[.results[] | select(.successful==true)] | length' <pre_scan>.json

# How many passed after?
jq '[.results[] | select(.successful==true)] | length' <post_scan>.json
```

If the second number is significantly higher than the first, the role is working as intended.

## How to read `PLAY RECAP`

After each converge, Ansible prints a one-line summary like:

```
PLAY RECAP ********************************************************
rhel9-cis-qa : ok=238  changed=73  unreachable=0  failed=0  skipped=547  rescued=0  ignored=0
```

| Counter | What it means |
|---|---|
| `ok` | Tasks that ran and finished successfully (no state change needed, or already in desired state) |
| `changed` | Tasks that modified the system (installed a package, edited a file, etc.) |
| `failed` | Tasks that errored out. **MUST BE 0** for the run to be considered passing. |
| `skipped` | Tasks gated off by `when:` conditions (often because `system_is_container: true` skips container-incompatible work) |
| `rescued` / `ignored` | Block-level error handling - typically 0 |

**Idempotency expectation:** the second `converge` should show `changed=0` (or near zero) - the system was already in the desired state. A high `changed` count on the second run means a task is not idempotent and needs fixing.

## Why some audit failures are expected (even after the role passes)

The post-scan will still show some controls failing. Most fall into three buckets that aren't role bugs - they're inherent to containerised testing:

1. **SSH-config controls** (banner, ciphers, KexAlgorithms, MACs, idle timeouts, login grace time): these check `/etc/ssh/sshd_config`, which doesn't exist because `openssh-server` is intentionally NOT installed (running sshd inside Docker is an anti-pattern; containers use `docker exec` for shell access). The role's `when: rhel9cis_ssh_required` gate handles this correctly on real hosts.

2. **User-state controls** (password complexity, password lifetime, dotfile audit): need real interactive users (UID >= 1000) with shadow entries and home directories. Containers only have system accounts, so the controls can't satisfy their preconditions.

3. **Kernel / mount controls**: any control gated by `not system_is_container` is intentionally skipped during remediation (auditd, kernel sysctls, mount options, partition checks) because containers share the host kernel. Audit still runs the goss tests, so they report as failing.

None of these warrant fixing the role. They're the expected delta between a containerised test and a real RHEL 9 host.

## Common gotchas

| Symptom | Likely cause | Fix |
|---|---|---|
| `molecule converge` errors with "container not running" | Stale container from a previous interrupted run | Run `molecule destroy` first, then retry |
| Pre-task fails with "Failed to download metadata" | UBI image can't reach repos, or no network | Check Docker network; some packages may be unavailable in UBI - that's expected (see `ignore_errors` in `ubi/prepare.yml`) |
| Converge #2 fails on a task that passed in #1 | Ansible 2.19+ struct-vs-string type-check tripping a `when:` clause | Inspect the offending task's `when:` - look for quoted-string-as-boolean bugs |
| `Conditional result (True) was derived from value of type 'str'` | Ansible 2.19+ rejects when-clauses whose final value is a non-boolean string | Remove the quotes; the RHS should be a bare Jinja expression |
| `verify` step empty / passes trivially | Expected - this role's primary validation is the goss audit JSONs, not molecule's `verifier:` plays | Inspect the audit JSONs instead |

## Why no Ansible pinning is needed

RHEL 9 / Rocky 9 ship Python 3.9 by default with full `dnf` Python bindings, so Ansible 2.19+ runs cleanly on managed nodes. Use any current Ansible venv.

## Reference: what's in the default scenario

| File | Purpose |
|---|---|
| `molecule.yml` | Driver: docker. Image: `rockylinux/rockylinux:9-ubi-init` on `linux/arm64`. Host vars listed in the next table. |
| `prepare.yml` | Bootstraps minimal Rocky 9 UBI via `raw` (python3, sudo, iproute, openssh), then installs CIS supporting packages. Stubs `/etc/default/grub` so GRUB-tag tasks don't fail in the container. |
| `converge.yml` | Sets root password (so PAM tasks don't lock us out), includes the role. |

## Reference: host vars (in `molecule/default/molecule.yml`)

| Override | Default | Purpose |
|---|---|---|
| `audit_output_destination` | `<working_dir>/_temp_fetched_audits/` | Where fetched audit JSONs land. Pinned outside the role tree so they don't pollute git. |
| `rhel9cis_disruption_high` | `true` (molecule default) | Exercises high-disruption code paths (account locks, password lifetime resets, sysctl reloads). Safe in throwaway containers; risky on real hosts. Defaults to `false` in `defaults/main.yml`. |
| `fetch_audit_output` | `true` | Auto-copies audit JSONs out of the container to `audit_output_destination`. |
| `system_is_container` | `true` | Gates container-incompatible tasks (auditd, kernel sysctls, mount changes, GRUB, etc.). |
| `skip_reboot` | `true` | Suppresses reboot handlers (containers can't reboot). |

## Overriding the audit branch

The audit clone branch is set in `vars/audit.yml` as `audit_git_version: "benchmark_{{ benchmark_version }}"` (currently `benchmark_v2.0.0` via `benchmark_version` in `defaults/main.yml`). That file is loaded with role-vars precedence, so values in `converge.yml` or `molecule.yml` `host_vars` **cannot** override it.

For normal molecule runs, no override is needed. When QA'ing an unpublished branch on `RHEL9-CIS-Audit`, pass `--extra-vars` after the `--` separator (the only precedence level that wins over `vars/audit.yml`):

```bash
# Single converge against a QA audit branch
molecule converge -- --extra-vars 'audit_git_version=<your-qa-branch>'

# ubi scenario
molecule -s ubi converge -- --extra-vars 'audit_git_version=<your-qa-branch>'

# Full gating pair (destroy, converge with QA branch, idempotency check, verify)
molecule destroy && molecule converge -- --extra-vars 'audit_git_version=<your-qa-branch>' && molecule converge && molecule verify
```

Replace `<your-qa-branch>` with the git branch or tag on `RHEL9-CIS-Audit` (for example `benchmark_v2.0.0` or a feature branch name). The branch must exist on the remote before converge runs.

## Where to ask for help

- This role's open issues: `github.com/ansible-lockdown/RHEL9-CIS/issues`
- Ansible Lockdown Discord (linked from the role README badge)
- Molecule docs: `molecule.readthedocs.io`
- Goss output format: `github.com/goss-org/goss`
