#!/bin/bash


# python manage.py makemigrations 
# python manage.py makemigrations users
# python manage.py makemigrations journals
# python manage.py showmigrations
# python manage.py migrate
gunicorn 'journaling_project.wsgi' --bind=0.0.0.0:8000 --workers=2