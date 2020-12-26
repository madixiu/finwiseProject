#!/bin/bash

#cd backend
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations users
python3 manage.py migrate users
python3 manage.py makemigrations
python3 manage.py migrate --no-input
gunicorn backend.wsgi -b 0.0.0.0:8000
# daphne -p 8000 backend.asgi:application