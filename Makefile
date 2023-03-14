VENV = $(CURDIR)/.venv

PYTHON = python
PIP = $(PYTHON) -m pip

ifeq ($(SHELL), fish)
	ACTIVATE = source $(VENV)/bin/activate.fish
	ACTIVATE_VENV = if test -z $$VIRTUAL_ENV; $(ACTIVATE) && $(SHELL); end
else
	ACTIVATE = . $(VENV)/bin/activate
	ACTIVATE_VENV = if [ -z $${VIRTUAL_ENV} ]; then $(ACTIVATE) && $(SHELL); fi
endif

activate: | $(VENV)
	$(ACTIVATE_VENV)

install: $(VENV)

$(VENV): requirements.txt
	if test ! -d $(VENV); then \
		$(PYTHON) -m venv $(VENV); \
	fi
	$(ACTIVATE) && $(PIP) install -r requirements.txt
	touch $(VENV)

.PHONY: install activate
