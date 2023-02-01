install:
	poetry install

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

test-cov:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

PORT ?= 8000
start:
	python manage.py runserver 0.0.0.0:$(PORT)

server:
	poetry run python manage.py runserver 0.0.0.0:$(PORT)

req:
	poetry export -f requirements.txt -o requirements.txt

translate:
	django-admin makemessages --ignore="static" --ignore=".env"  -l ru

compile:
	django-admin compilemessages

secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'
