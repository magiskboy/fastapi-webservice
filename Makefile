all: dev

dev: app
	@appcli dev

test:
	python -m pytest

lint:
	PYTHONPATH=. python linter.py --fail-under 9.5 app
	PYTHONPATH=. mypy app

clean:
	@rm -rf coverage.xml .coverage htmlcov
