#!/bin/bash

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn for production
# gunicorn investmenttracker.wsgi:application --bind 0.0.0.0:8000

python manage.py runserver 0.0.0.0:8000