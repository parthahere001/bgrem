#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python3 manage.py collectstatic --no-input
python3 manage.py migrate
python3 manage.py createsuperuser
partha
a@a.com
1234
1234
python3 manage.py createsuperuser
komal
k@k.com
123
123
