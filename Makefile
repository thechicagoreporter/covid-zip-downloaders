################################################################################
#
# Download COVID ZIP code data
#
# Run `make help` to see all commands.
#
# This is an auto-documenting Makefile:
#
# Add sections to help with a line like:
#
#  ##@ Section Name
#
# Add commands by following a target line with a double-# comment
# like this:
#
#  clean: ## Delete all files".
#
################################################################################

# Include .env configuration
include .env
export

# Activate Python environment
PYENV = pipenv run


##@ Basic usage

.PHONY: all
all: snapshot ## Download all data

.PHONY: clean
clean: rm/external ## Clean local data files

.PHONY: rm/%
rm/%: # Remove data/% where % is a directory name
	rm -rf data/$*/*

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z\%\\.\/_-]+:.*?##/ { printf "\033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Download

data/external/%.json:
	$(PYENV) python processors/$*.py $@

##@ Setup

.PHONY: install
install: install/python

.PHONY: install/python
install/python: ## Install Python dependencies (usually only required once)
	pipenv install