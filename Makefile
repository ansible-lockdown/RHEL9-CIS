.PHONY: all galaxy-install ansible-list yamllint pip-requirements help


GALAXY=ansible-galaxy
ANSIBLE_LINT=ansible-lint
ANSIBLE_FILE=site.yml

all: help

help:
	@echo "Make command examples for Ansible"
	@echo "Command for assisting with ansible setup"
	@echo "    galaxy-install                     to install roles using ansible-galaxy"
	@echo "    ansible-lint                       to lint playbook files"
	@echo "    yamllint                           to lint playbook files"
	@echo "    pip-requirements                   add pip required file"


galaxy-install:
	$(GALAXY) install -r ./collections/requirements.yml

ansible-lint:
	$(ANSIBLE-LINT) $(ANSIBLE_FILE)

yamllint:
	git ls-files "*.yml"|xargs yamllint

pip-requirements:
	@echo 'Python dependencies:'
	@cat requirements.txt
	$(ANSIBLE_LINT) install -r requirements.txt

