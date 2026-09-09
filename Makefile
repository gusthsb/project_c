# Variáveis
PYTHON = python3

# Roda o seu cassino
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