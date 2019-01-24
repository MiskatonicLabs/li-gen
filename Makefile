.PHONY: env run test lint requires docs
.DEFAULT: env

env:
	@poetry install

run:
	@source .env; poetry run flask run

test:
	@source .env; poetry run coverage run --branch -m unittest discover && poetry run coverage html

requires:
	@poetry show --no-dev | tr -s " " | sed 's/ /==/' | sed 's/ .*//' > requirements.txt

lint:
	@poetry run isort --virtual-env .venv li_gen/*.py && poetry run flake8

docs:
	@poetry run sphinx-apidoc -f -o docs/source/ li_gen ./tests/*.py
	@cd docs && make html
