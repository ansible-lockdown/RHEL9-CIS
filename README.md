
# RHEL 9 CIS

## v1.0.0 - released Dec 2022

![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL9-CIS/CommunityToDevel?label=Devel%20Build%20Status&style=plastic)
![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL9-CIS/DevelToMain?label=Main%20Build%20Status&style=plastic)
![Release](https://img.shields.io/github/v/release/ansible-lockdown/RHEL9-CIS?style=plastic)

Configure RHEL 9 machine to be [CIS](https://www.cisecurity.org/cis-benchmarks/)

Based on [CIS RedHat Enterprise Linux 9 Benchmark v1.0.0. - 11-30-2022 ](https://www.cisecurity.org/cis-benchmarks/)

## Join us

On our [Discord Server](https://discord.io/ansible-lockdown) to ask questions, discuss features, or just chat with other Ansible-Lockdown users

## Caution(s)

This role **will make changes to the system** which may have unintended concequences.

This role was developed against a clean install of the Operating System. If you are implimenting to an existing system please review this role for any site specific changes that are needed.

To use release version please point to main branch

## Documentation

- [Readthedocs](https://ansible-lockdown.readthedocs.io/en/latest/)
- [Getting Started](https://www.lockdownenterprise.com/docs/getting-started-with-lockdown)
- [Customizing Roles](https://www.lockdownenterprise.com/docs/customizing-lockdown-enterprise)
- [Per-Host Configuration](https://www.lockdownenterprise.com/docs/per-host-lockdown-enterprise-configuration)
- [Getting the Most Out of the Role](https://www.lockdownenterprise.com/docs/get-the-most-out-of-lockdown-enterprise)

## Requirements

RHEL 9
Almalinux 9
Rocky 9

- Access to download or add the goss binary and content to the system if using auditing (other options are available on how to get the content to the system.)

- makefile - this is there purely for testing and initial setup purposes.

## General

- Basic knowledge of Ansible, below are some links to the Ansible documentation to help get started if you are unfamiliar with Ansible
  - [Main Ansible documentation page](https://docs.ansible.com)
  - [Ansible Getting Started](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
  - [Tower User Guide](https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html)
  - [Ansible Community Info](https://docs.ansible.com/ansible/latest/community/index.html)

- Functioning Ansible and/or Tower Installed, configured, and running. This includes all of the base Ansible/Tower configurations, needed packages installed, and infrastructure setup.
- Please read through the tasks in this role to gain an understanding of what each control is doing.
  - Some of the tasks are disruptive and can have unintended consiquences in a live production system. Also familiarize yourself with the variables in the defaults/main.yml file

## Dependencies

- Python3
- Ansible 2.9+
- python-def (should be included in RHEL 9)
- libselinux-python
- pip packages
  - jmespath ( complete list found in requirements.txt)
- collections found in collections/requirememnts.yml

## Role Variables

This role is designed that the end user should not have to edit the tasks themselves. All customizing should be done via the defaults/main.yml file or with extra vars within the project, job, workflow, etc. These variables can be found [here](https://github.com/ansible-lockdown/RHEL9-CIS/wiki/Main-Variables) in the Main Variables Wiki page. All variables are listed there along with descriptions.

## Tags

There are many tags available for added control precision. Each control has it's own set of tags noting what level, if it's scored/notscored, what OS element it relates to, if it's a patch or audit, and the rule number.

Below is an example of the tag section from a control within this role. Using this example if you set your run to skip all controls with the tag services, this task will be skipped. The opposite can also happen where you run only controls tagged with services.

```txt
      tags:
      - level1-server
      - level1-workstation
      - scored
      - avahi
      - services
      - patch
      - rule_2.2.4
```

### Known Issues

CIS 1.2.4 - repo_gpgcheck is not carried out for RedHat hosts as the  default repos do not have this function. Rocky and Alma not affected.
Variable used to unset.
rhel9cis_rhel_default_repo: true  # to be set to false if using repo that does have this ability
