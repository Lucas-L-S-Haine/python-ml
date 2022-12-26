USER_SHELL = /bin/bash
VENV = .venv
USER_VIRTUAL_ENVIRONMENT = $(CURDIR)/$(VENV)

activate: | $(USER_VIRTUAL_ENVIRONMENT)
	if test -z "$${VIRTUAL_ENV}"; then \
		. $(USER_VIRTUAL_ENVIRONMENT)/bin/activate && $(USER_SHELL); \
	fi

install: $(USER_VIRTUAL_ENVIRONMENT)

$(USER_VIRTUAL_ENVIRONMENT): requirements.txt
	if test ! -d $(USER_VIRTUAL_ENVIRONMENT); then \
		python -m venv $(USER_VIRTUAL_ENVIRONMENT); \
	fi
	. $(USER_VIRTUAL_ENVIRONMENT)/bin/activate && pip install -r requirements.txt
	touch $(USER_VIRTUAL_ENVIRONMENT)

.PHONY: install activate
