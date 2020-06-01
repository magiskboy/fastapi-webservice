all: deps dev

deps: requirements.txt requirements-dev.txt
	pip install -r requirements-dev.txt

dev: app asgi.py 
	uvicorn asgi:app --reload --workers 1

test:
	python -m pytest

lint:
	PYTHONPATH=. python linter.py --fail-under 9.5 app
	PYTHONPATH=. mypy asgi.py

clean:
	@rm -rf coverage.xml .coverage htmlcov
