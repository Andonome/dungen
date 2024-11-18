VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

GRAPHVIZ_CHECK := $(shell which dot 2>/dev/null)

run: $(VENV)/bin/activate
	$(PYTHON) main.py 2>/dev/null

$(VENV)/bin/activate: requirements.txt check-graphviz
	python3 -m venv $(VENV)
	echo '*' > $(VENV)/.gitignore
	$(PIP) install -r requirements.txt

check-graphviz:
ifndef GRAPHVIZ_CHECK
	$(error "Graphviz not found. Please install graphviz system package first (e.g., 'sudo apt install graphviz' or 'brew install graphviz')")
endif

clean:
	$(RM) -r __pycache__
	$(RM) -r $(VENV)
	$(RM) *.pdf
	$(RM) *.gv