VENV=./venv
PYTHON=./venv/bin/python

all:
	@echo "Targets:"
	@echo " runserver: run a single process with in-memory channels"
	@echo " start:     multi-process setup using honcho and Redis"


virtualenv: $(VENV)/stamp

$(VENV)/stamp: requirements.txt
	[ -f $(PYTHON) ] || virtualenv -p python3 venv
	$(VENV)/bin/pip3 install -r requirements.txt
	touch $(VENV)/stamp

runserver: virtualenv
	$(PYTHON) chan/manage.py runserver

start: virtualenv
	PATH="$(VENV)/bin:$(PATH)" honcho start
