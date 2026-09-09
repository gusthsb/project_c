PYTHON = python3

run:
	$(PYTHON) main.py

format:
	black .

lint:
	flake8 .

typecheck:
	mypy .

check: format lint typecheck

clean:
	rm -rf __pycache__ .mypy_cache