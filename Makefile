VENV=./venv
PYTHON=./venv/bin/python

all:
	echo "Targets: virtualenv, run"

virtualenv: $(VENV)/stamp

$(VENV)/stamp: requirements.txt
	virtualenv -p python3 venv
	$(VENV)/bin/pip3 install -r requirements.txt
	touch $(VENV)/stamp

run: virtualenv
	$(PYTHON) chan/manage.py runserver
