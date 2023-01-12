install:
	poetry install

lint:
	poetry run flake8 task_manager

server:
	python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 127.0.0.1:$(PORT) task_manager.wsgi