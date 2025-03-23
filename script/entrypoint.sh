#!/bin/bash

python manage.py migrate

python manage.py collectstatic --noinput

# gunicorn investmenttracker.wsgi:application --bind

python manage.py runserver 0.0.0.0:8000