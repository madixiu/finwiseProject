#!/bin/bash

#cd backend
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations users
python3 manage.py migrate users
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000