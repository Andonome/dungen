VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) main.py 2>/dev/null


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	echo '*' > $(VENV)/.gitignore
	$(PIP) install -r requirements.txt


clean:
	$(RM) -r __pycache__
	$(RM) -r $(VENV)
	$(RM) *.pdf
	$(RM) *.gv
