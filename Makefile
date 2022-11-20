USER_SHELL = /bin/bash

activate: | .venv
	if test -z "$${VIRTUAL_ENV}"; then \
		. .venv/bin/activate && $(USER_SHELL); \
	fi

install: .venv

.venv: requirements.txt
	if test ! -d .venv; then \
		python -m venv .venv; \
	fi
	. .venv/bin/activate && pip install -r requirements.txt
	touch .venv

.PHONY: install activate
