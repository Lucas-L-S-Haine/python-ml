include get_shell.mk

VENV = $(CURDIR)/.venv

PYTHON = python
PIP = $(PYTHON) -m pip

activate: | $(VENV)
	$(ACTIVATE_VENV)

install: $(VENV)

$(VENV): requirements.txt
	$(IF) test ! -d $(VENV); $(THEN) \
		$(PYTHON) -m venv $(VENV); \
	$(FI)
	$(ACTIVATE) && $(PIP) install -r requirements.txt
	touch $(VENV)

.PHONY: install activate
