SHELL=/bin/bash
.DEFAULT_GOAL=none


### help actionss
help:
	@echo 'Makefile for autosky app                                                                            '
	@echo '                                                                                                    '
	@echo 'Usage:                                                                                              '
	@echo '                                                                                                    '
	@echo '    make install           Install python packages (with pip, from requirements.txt)                '
	@echo '    make install-dev       Install python packages (with pip, from requirements-dev.txt)            '
	@echo '    make config            Create folders and files to up application                               '
	@echo '                                                                                                    '
	@echo '    make pipenv-sync       Install python packages with pipenv (from Pipfile.lock, without update)  '
	@echo '    make pipenv-update     Update the version of python packages of project dependencies            '
	@echo '    make pipenv-lock       Create lock files to pip and pipenv (Pipfile.lock and requirements.txt)  '

### actions to clean project files
clean: clean-cache

clean-cache:
	rm -fr htmlcov;
	rm -fr .cache;
	rm -fr .coverage;
	rm -fr .pytest_cache;
	rm -fr junit.xml coverage.xml;
	find . -iname '*.pyc' -delete;
	find . -iname '*.pyo' -delete;
	find . -name '*,cover' -delete;
	find . -iname __pycache__ -delete;

### actions to install env
config:
	mkdir -p ./{logs,static}

install:
	make config && pip install -r requirements.txt

install-dev:
	make config && pip install -r requirements-dev.txt


### actions to upgrade packages (with pipenv)
pipenv-check:
	pipenv > /dev/null || pip install pipenv

pipenv-sync:
	make pipenv-check && pipenv sync --sequential --dev

pipenv-update:
	make pipenv-sync && pipenv install --sequential --dev && make pipenv-lock

pipenv-lock: config pipenv-check
	make pipenv-check && pipenv lock && pipenv lock -r > requirements.txt && pipenv lock --dev -r > requirements-dev.txt && sed -i '1 a -r requirements.txt' requirements-dev.txt
