release: python manage.py migrate
web: gunicorn task_manager.wsgi --host=0.0.0.0 --port=${PORT:-8000}