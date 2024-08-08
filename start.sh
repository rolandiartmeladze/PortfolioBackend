#!/bin/bash

# Requirements-ის ინსტალაცია
pip install -r requirements.txt

# მონაცემთა ბაზის მიგრაცია
python3 manage.py migrate

# Django სერვერის გაშვება
python3 manage.py runserver 0.0.0.0:8000
