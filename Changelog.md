# Changes to rhel9CIS

## 1.1.6 - Based on CIS v1.0.0

- #190 - thanks to @ipruteanu-sie
  - addressed requirements in PR with alternate method
- #191 - thanks to @numericillustration
  - Addressed authselect for pam
- #193 thanks to brakkio86

## 1.1.5 - Based on CIS v1.0.0

- added new interactive user discoveries
  - updated controls 6.2.10-6.2.14
- audit
  - steps moved to prelim
  - update to coipy and archive logic and variables
- removed vars not used
- updated quotes used in mode tasks
- pre-commit update
- issues addressed
  - #190 thanks to @ipruteanu-sie
    - aligned logic for user shadow suite params (aligned with other repos)
    - new variables to force changes to existing users added 5.6.1.1 - 5.6.1.2
  - #198 thanks to @brakkio86

## 1.1.4 - Based on CIS v1.0.0

- 1.2.1 new option for a new system to import gpg key for 1.2.1 to pass redhat only
- thanks to @ipruteanu-sie
  - #156
  - #165
  - #180
  - #181
  - #183
  - #184

## 1.1.3 - Based on CIS v1.0.0

- updated goss binary to 0.4.4
- moved majority of audit variables to vars/audit.yml
- new function to enable audit_only using remediation
- removed some dupes in audit config

## 1.1.2 - Based on CIS v1.0.0

- updated audit binary versions - aligned with rhel9-cis-audit
- lint updates
- .secrets updated
- file mode quoted
- updated 5.6.5 thansk to feedback from S!ghs on discord community

## 1.1.1 - Based on CIS v1.0.0

- thanks to @agbrowne
  - [#90](https://github.com/ansible-lockdown/RHEL9-CIS/issues/90)

- thanks to @mnasiadka
  - [#54](https://github.com/ansible-lockdown/RHEL9-CIS/pull/54)

## 1.1.0

- new workflow configuration
  - Allowing devel and main configs
  - IaC code found in alternate repo for easier mgmt
- Added pre-commit config - Does not have to be used but can improve things
  - .pre-commit-config.yaml
  - .secrets.baseline
  - gitleaks and secrets detection

- updated to logic in 5.6.5
- lint updates to 6.1.x
- readme updates
- audit control updates and variable name changes
  - ability to run audit on arm64(e.g. pi or M1/2) too thanks to @lucab85 #77
- tidy up README adopted PR #78 thanks to @lucab85
- moved Makefile requirements to .config/
- removed .ansible.cfg and local.yml

## 1.0.10

- [#72](https://github.com/ansible-lockdown/RHEL9-CIS/issues/72)
  - Only run check when paybook user not a superuser
- fix for 5.5.3 thanks to @nrg-fv

## 1.0.9

fixed assert for user password set

thanks to @byjunks
[#66](https://github.com/ansible-lockdown/RHEL9-CIS/issues/66)

## 1.0.8

rule_1.10 improvements allowing for module checking (useful for AD)

## 1.0.7

lint and yaml updates
improvements to 6.1.10, 6.1.11, 6.1.13, 6.1.14
4.1.3.6 updated on process discovery

## 1.0.6

updated yamllint as galaxy doesn't honour local settings
removed empty lines in files

## 1.0.5

updated yamllint
removed empty lines after lint
initial molecule added
galaxy workflow updated

## 1.0.4

#40 tmp systemd file variable naming update
#41 5.3.7 logic and rewrite - tidy up prelim for sugroup work - audit updated

## 1.0.3

Update to auditd components improve idempotency and tidy up
Added a warning to check diff if any changes to template file (if template file exists) else its new.
workflow update to remove the urandom update
skip 5.6.6 root password check
variable naming
OracleLinux support added
#38 journald restart amendment thanks to @bdwyertech

## 1.0.2

thanks to @smatterchew
#30 ability to change sshd config file to use dropin file instead.

thanks to @I-am-MoS
#34 create user.cfg if not present

Aligned benchmark audit version with remediate release

## 1.0.1

Control 6_2_16 new variable added thanks to @dulin_gnet on rhel8
Will not follow symlink in home directories and amend permissions.

- rhel_09_6_2_16_home_follow_symlink: false

## Initial CIS v1.0.0 - released Dec 2022

### Official CIS release

Jan-2023 release

- updated ansible minimum to 2.10
- Lint file updates and improvements
- auditd now shows diff ater initial template added
- many control rewritten
- Many controls moved ID references
- Audit updates aligned
- Command warn arg removed
- Ansible 2.14 now supported
- makefile added (hopefully help some)
- fqcn added to all controls
- some controls rewritten using module rather than shell
- typo fixes from rhel_08 inheritance
- workflow update for 5.6.6 to set random root password to allow for testing
- incorporates issues
  - #23
  - #24
- New option to add faillock for users without authselect - defaults/main 5.4.2

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
