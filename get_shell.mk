SHELL := $(shell echo $(SHELL) | python -c "import subprocess as sp; \
	shell = sp.check_output(['ps', '-o', 'comm=']).decode('utf-8').split(); \
	print(shell[0] if shell[2] == 'sh' else shell[2])")

ifeq ($(notdir $(SHELL)), fish)
	ACTIVATE = source $(VENV)/bin/activate.fish
	ACTIVATE_VENV = if test -z $$VIRTUAL_ENV; $(ACTIVATE) && $(SHELL) $(SHELL_FLAGS); end
	IF := if
	FI := end
else
	ACTIVATE = . $(VENV)/bin/activate
	ACTIVATE_VENV = if [ -z $${VIRTUAL_ENV} ]; then $(ACTIVATE) && $(SHELL) $(SHELL_FLAGS); fi
	IF   := if
	THEN := then
	FI   := fi
endif
