# Changes to RHEL9CIS

## 2.0.5 - Based on CIS v2.0.0

- QA Fixes
- .j2 Branding Update
- Added rhel9cis_uses_root variable definition for 5.4.2.5 root PATH integrity task
- fixed spelling and grammar across defaults/main.yml, Changelog.md, README.md, tasks/main.yml, and vars/main.yml
- Fixed incorrect product reference in vars/main.yml comment (ubtu24cis -> rhel9cis)
- Fixed broken Changelog link in README.md (case mismatch)
- Added var-naming[read-only] to ansible-lint skip list for molecule files
- Bootloader password logic updated with salt and hash options
- Added passlib dependency documentation for bootloader password hash
- Updated company title
- Tidied up comments and variables for bootloader password
- Removed scheduled tasks
- Fixed typo thanks to Eugene @Frequentis
- Unused variable audit: wired up all unused variables, removed legacy references
- Updated chrony template to use rhel9cis_chrony_server_makestep, rtcsync, and minsources variables instead of hardcoded values
- Wired up rhel9cis_authselect_custom_profile_create toggle in authselect profile creation task
- Fixed task 5.3.3.2.7/5.3.3.2.8 mislabeling: separated password quality enforce and root enforce into correct tasks
- Wired up audit_capture_files_dir in audit_only workflow for file capture to control node
- Clarified rhel9cis_root_unlock_time documentation for commented-out alternative usage
- Removed legacy rhel9cis_rule_1_1_10 from molecule converge files and is_container.yml
- Fixed wrong variable name rhel9cis_unowned_group to rhel9cis_ungrouped_group in tasks/section_7/cis_7.1.x.yml
- Added rhel9cis_install_network_manager toggle to 3.1.2 wireless interfaces task

## 2.0.4 - Based on CIS v2.0.0

addressed issue #419, thank you @aaronk1
addressed issue #418 thank you @bbaassssiiee
Added better sysctl logic to disable IPv6
Added option to disable IPv6 via sysctl (original method) or via the kernel
pre-commit updates
public issue #410 thanks to @kpi-nourman
public issue #413 thanks to @bbaassssiiee
Public issues incorporated
Workflow updates
Pre-commit updates
README latest versions
Audit improvements and max-concurrent option added
Benchmark version variable in audit template
fixed typo thanks to @fragglexarmy #393
fixed typo thanks to @trumbaut #397 & #399
updated auditd template to be 2.19 compliant
PR345 thanks to thulium-drake boot password hash - if used needs passlib module
tidy up tags on tasks/main.yml

## 2.0.3 - Based on CIS v2.0.0

- Thank you @fragglexarmy
  - addressed Public issue 387
- Addressed Public issue 382 to improve regex logic on 5.4.2.4
- Improvement on crypto policy managed controls with var logic
- Thanks to @polski-g
  - addressed issue 384
- update command to shell module on tasks
- Thanks to @numericillustration
  - Public PR 380
  - systemd_service rolled back to systemd for < ansible 2.14
- Thanks to @bgro and @Kodebach
  - Public PR 371
  - updated to user sudo check 5.2.4
- Thanks to @DianaMariaDDM
  - Public PR 367
  - updated several typos
- Thanks to @polski-g
  - Public PR 364
  - gdm section 1.8 improvements
- Thanks to @chrispipo
  - Public PR 350
  - change insert before for rsyslog setting
- Thanks to @thesmilinglord
  - public issue 377
  - change 1.3 from include task to import for tagging
- Thanks to @Fredouye
  - public issue 372
  - allow password with different locale

## 2.0.2 - Based on CIS v2.0.0

- Update to audit_only to allow fetching results
- resolved false warning for fetch audit
- fix root user check
- Improved documentation and variable compilation for crypto policies
- Addresses #318 - Thank you @kodebach & @bgro
  - Improved logic for 5.2.4 to exclude rhel9cis_sudoers_exclude_nopasswd_list in pre-check tasks/main.yml

## 2.0.1 - Based on CIS v2.0.0

- Thanks to @polski-g several issues and improvements added
- Improved testing for 50-redhat.conf for ssh
- 5.1.x regexp improvements
- Improved root password check
- egrep command changed to grep -E

## 2.0.0 - Based on CIS v2.0.0

- #322, #325 - thanks to @mindrb
- #320 - thanks to @anup-ad

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
  - update to copy and archive logic and variables
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
- updated 5.6.5 thanks to feedback from S!ghs on discord community

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
  - Only run check when playbook user not a superuser
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
- auditd now shows diff after initial template added
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
  -Extended the auditd config required value for auditd space left percentage (not part of CIS Benchmark but required for auditd to run correctly in some cases)

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
- updated to rhel8cis v2.0 benchmark requirements
- removed iptables firewall controls (not valid on rhel9)
- added more to logrotate 4.3.x - sure to logrotate now a separate package
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
- 3.4.2 improved checks for package presence
- changed to assert for OS/release and ansible version

## Initial

- based on RHEL8 currently as RH or CIS not GA
- Changes to systctl, auditd, aide cron changes to utilise templates - see issue #1
- Collection statement added to meta/main.yml using only community-general
- aide crontab moved to template due to module change
