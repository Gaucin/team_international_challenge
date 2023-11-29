PYTHONPATH := ./

export PYTHONPATH

.PHONY: run
run:
	python app/run.py

.PHONY: pytestcov
pytestcov:
	pytest --cov-fail-under 95 --cov-report term-missing --cov=app -s tests

.PHONY: flake
flake:
	flake8 --ignore E305 --exclude .git,__pycache__ --max-line-length=90

.PHONY: black
black:
	black . -l 90

