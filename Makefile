PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PELICAN := $(VENV)/bin/pelican

.PHONY: install serve build clean new

install:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

serve:
	$(PELICAN) content -s pelicanconf.py -lr -p 8000

build:
	$(PELICAN) content -s publishconf.py

clean:
	rm -rf output cache __pycache__ .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete

new:
	@test -n "$(TITLE)" || (echo 'Usage: make new TITLE="Mi nuevo ensayo"' && exit 1)
	$(VENV)/bin/python scripts/new_post.py "$(TITLE)"
