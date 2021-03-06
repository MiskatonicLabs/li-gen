.PHONY: env local_run run test lint requires docs migrate migrations
.DEFAULT: env

env:
	@poetry install

local_run:
	@source .env; poetry run python manage.py runserver 0.0.0.0:8000 --settings=li_gen.settings.local

run:
	@source .env; poetry run gunicorn li_gen.wsgi --log-file -

static:
	@source .env; poetry run python li_gen/manage.py collectstatic

test:
	@source .env; poetry run coverage run --branch -m unittest discover && poetry run coverage html

requires:
	@poetry show --no-dev | tr -s " " | sed 's/ /==/' | sed 's/ .*//' > requirements.txt

lint:
	@poetry run isort --virtual-env .venv li_gen/*.py && poetry run flake8

migrations:
	@source .env; poetry run python ./manage.py makemigrations

migrate:
	@source .env; poetry run python ./manage.py migrate

docs:
	@poetry run sphinx-apidoc -f -o docs/source/ li_gen ./tests/*.py
	@cd docs && make html
