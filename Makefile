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

ROOT_DIR:=$(shell pwd)

help:
	@echo ""
	@echo "Please use ${BOLD}'make <target>'${NONE}  where ${BOLD}<target>${NONE} is one of"
	@echo ""
	@echo "${UNDERLINE} build-dev-environment: ${NONE}"
	@echo " ${BOLD}build-dev-environment : ${GREEN} Creates the Development Environment${NONE}"
	@echo ""
	@echo "${UNDERLINE} Upgrade and Install all dependencies: ${NONE}"
	@echo " ${BOLD}install_open-development-environmentdependencies : ${GREEN} Opens the devcontainer${NONE}"
	@echo ""

# Development Environments
build-dev-environment:
	@echo "Building & starting the python local environment"
	docker compose -f $(ROOT_DIR)/docker/dev/docker-compose.yml up --build

open-development-environment: 
	devcontainer open ./src

init: create_virtual_env install_dependencies check_py

run_app:
	$(PYTHON) app.py
