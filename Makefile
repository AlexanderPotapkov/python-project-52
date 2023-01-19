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

PORT ?= 8000
start:
	poetry run python manage.py runserver 0.0.0.0:$(PORT)

req:
	poetry export -f requirements.txt -o requirements.txt

secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'
