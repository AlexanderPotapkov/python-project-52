# Task manager
[![Actions Status](https://github.com/AlexanderPotapkov/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/AlexanderPotapkov/python-project-52/actions)
[![CI](https://github.com/AlexanderPotapkov/python-project-52/workflows/CI/badge.svg)](https://github.com/AlexanderPotapkov/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/11d0dfcbd06d82705bd1/maintainability)](https://codeclimate.com/github/AlexanderPotapkov/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/11d0dfcbd06d82705bd1/test_coverage)](https://codeclimate.com/github/AlexanderPotapkov/python-project-52/test_coverage)

[Web-application on Railway](https://task-manager-potapkov-alex.up.railway.app/)

The web application is a task management system. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.

### Installation:
```
    pip install "git+https://github.com/AlexanderPotapkov/python-project-52.git"
    pip install -r requirements.txt
```
### For start you need to create .env file in root of project with values:
```
    SECRET_KEY='Django Secret Key'
    ROLLBAR_KEY='Rollbar Key'
    If you want to use SQLite:
        DB_ENGINE='SQLite'
    If you want to use PostgreSQL:
        POSTGRES_DB='DB name'
        POSTGRES_USER='user'
        POSTGRES_PASSWORD='password'
        POSTGRES_HOST='host'
        POSTGRES_PORT='port'
```
### For local start:
```
    make server
```
