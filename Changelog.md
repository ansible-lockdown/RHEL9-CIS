# Changes to rhel9CIS

## Initial CIS v1.0.0 - released Dec 2022

### Official CIS release

Jan-2023 release

- Lint file updates and improvements
- Many controls moved ID references
- Audit updates aligned
- Command warn arg removed
- Ansible 2.14 now supported
- makefile added (hopefully help some)
- fqcn added to all controls
- some controls rewritten using module rather than shell
- typo fixes from rhel_08 inheritance
- workfolw update for 5.6.6 to set random root password to allow for testing
- incorporates issues
  - #23
  - #24

## 0.5

- audit path updated and output file name

### Taken from RHEL8-CIS issues and PRs

- #209 5.6.5 rewrite umask settings
- #220 tidy up and align variables
- #226 Thanks to Thulium-Drake
  -Extended the auditd config required value for auditd space left percentage (not part of CIS Benchmark but required fopr auditd to run correctly in some cases)

- #227 thanks to OscarElits
  - chrony files now RH expected locations
- #228 Thanks to benbulll
  - audit binary copy var missing

## 0.4

- Added assertion that ansible_user has password set for rule 5.3.4
- RockyLinux now supported - release since initial branches
- gpg check updates
- audit out dir now /opt
- lint updates and improvements
- workflow updates and improvements moved to rocky image
- selinux regexp improvements
- warning summary now at end of play
- advanced auditd options to exclude users in POST section
- Issues fixed thanks to fgierlinger
  - [#21](https://github.com/ansible-lockdown/RHEL9-CIS/issues/21)
  - [#22](https://github.com/ansible-lockdown/RHEL9-CIS/issues/22)

## 0.3

- update to auditd template
  - uses facts and template new variable
    - update_audit_template (default false)
- sysctl template updates and idempotency improvements
- container discovery usage improvements
- 3.4.1.5 discovery improvement
- 5.6.1.4 discovery improvement
- logrotate process logrotate.timer
- tidy up become:
- logic improvements

## 0.2

- not all controls work with rhel8 releases any longer
  - selinux disabled 1.6.1.4
  - logrotate - 4.3.x
- updated to rhel8cis v2.0 benchamrk requirements
- removed iptables firewall controls (not valid on rhel9)
- added more to logrotate 4.3.x - sure to logrotate now a seperate package
- grub path now standard to /boot/grub2/grub.cfg
- 1.6.1.4 from rh8 removed as selinux.cfg doesnt disable selinux any longer
- workflow update
- removed doc update

## 0.1

- change to include statements
- prelim and package facts discovery
- commands module removed and moved to shell
  - added

```yml
args:
    warn: false
```

- update boolean values to true/false
- 3.4.2 improved checks for p[ackage presence
- changed to assert for OS/release and ansible version

## Initial

- based on RHEL8 currently as RH or CIS not GA
- Changes to systctl, auditd, aide cron changes to utilise templates - see issue #1
- Collection statement added to meta/main.yml using only community-general
- aide crontab moved to template due to module change
