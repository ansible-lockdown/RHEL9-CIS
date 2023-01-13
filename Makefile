# TESTS

all: yamllint

yamllint:
	git ls-files "*.yml"|xargs yamllint

requirements:
	@echo 'Python dependencies:'
	@cat requirements.txt
	pip install -r requirements.txt
