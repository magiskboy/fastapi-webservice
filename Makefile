TAG = $(shell cat .git/refs/heads/master | cut -c1-8)

all: dev

deps:
	pip install -r requirements-dev.txt

dev: deps
	python app dev

test: deps
	python -m pytest

lint: deps
	PYTHONPATH=. python linter.py --fail-under 9.5 app
	PYTHONPATH=. mypy app

docker-build: Dockerfile .dockerignore
	docker build . -t nguyenkhacthanh/fastapi-boilerplate:m-$(TAG)

clean:
	@rm -rf \
		coverage.xml \
		.coverage \
		htmlcov \
		*.egg-info \
		dist \
		docs/build \
		docs/source/refs
