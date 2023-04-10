# formatting
NONE=\033[00m
RED=\033[01;31m
GREEN=\033[01;32m
YELLOW=\033[01;33m
PURPLE=\033[01;35m
CYAN=\033[01;36m
WHITE=\033[01;37m
BOLD=\033[1m
UNDERLINE=\033[4m

help:
	@echo ""
	@echo "Please use ${BOLD}'make <target>'${NONE}  where ${BOLD}<target>${NONE} is one of"
	@echo ""
	@echo "${UNDERLINE} Create a Virtual Environment: ${NONE}"
	@echo " ${BOLD}create_virtual_env : ${GREEN} Creates the virtual directory${NONE}"
	@echo ""
	@echo ""
	@echo "${UNDERLINE} Upgrade and Install all dependencies: ${NONE}"
	@echo " ${BOLD}install_dependencies : ${GREEN} Upgrading pip and installing 3rd party python dependencies${NONE}"
	@echo ""
	@echo ""
	@echo "${UNDERLINE} Check verisons of python and pip: ${NONE}"
	@echo " ${BOLD}check_py : ${GREEN} Shows the installed versions of Python and pip${NONE}"
	@echo ""
	@echo ""
	@echo "${UNDERLINE} Creates a Virtual Environment and installs all dependencies: ${NONE}"
	@echo " ${BOLD}init : ${GREEN} Creates the virtual directory${NONE}"
	@echo ""
	@echo ""
	@echo "${UNDERLINE} Run the program: ${NONE}"
	@echo " ${BOLD}run_main : ${GREEN} Runs the program (provided you have a main.py)${NONE}"
	@echo ""

VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip3

create_virtual_env:
	@echo Creating the virtual directory: $(VENV)
	rm -rf $(VENV)
	python3 -m venv $(VENV)

install_dependencies:
	@echo Upgrading pip and installing 3rd party python dependencies
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check_py:
	@echo Checking the Python and Pip versions in virtual environment
	$(PYTHON) --version
	$(PIP) --version

init: create_virtual_env install_dependencies check_py

run_app:
	$(PYTHON) app.py
