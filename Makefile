VENV=./venv

all:
	echo "Targets: virtualenv"

.PHONY: virtualenv
virtualenv:
	virtualenv -p python3 venv
	$(VENV)/bin/pip3 install -r requirements.txt
