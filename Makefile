venv = venv
mypy = $(venv)/bin/python3
pybin != realpath `command -v python`
version != basename $(pybin)
pip = $(venv)/bin/pip

output += $(wildcard $(venv))
output += $(wildcard *.pdf)
output += $(wildcard *.gv)
output += $(wildcard __pycache__)

out: run

$(pip):
	$(pybin) -m venv $(venv)

$(mypy): $(pip)

$(venv)/lib/$(version)/site-packages/: requirements.txt $(mypy)
	$(pip) install -r $<

ignore_file != dir .git/info/exclude || echo .gitignore

$(ignore_file): $(output)
	echo $^ | tr ' ' '\n' > $@

.PHONY: run
run: $(venv)/lib/$(version)/site-packages/ $(ignore_file)
	$(mypy) main.py

clean:
	$(RM) -r $(output)

