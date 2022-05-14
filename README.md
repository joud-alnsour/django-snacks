# Django-snacks
## Project:snacks_project
Author: Joud Alnsour<br>
Date: 2022-05-10<br>
Application Version: 1.0.0<br>
Django: 4.0.4
## Steps to get started
- Run following CLI commands
     - poetry new [django-snacks]
     - poetry install
     - poetry shell
     - poetry add django
     - django-admin start project [snacks_project]
     - python manage.py migrate
     - python manage.py createsuperuser
     - python manage.py startapp [snacks]
- Create your models, templates & views
- Run following CLI commands
     - python manage.py makemigrations
     - python manage.py migrate
## How to start the website 
- python manage.py runserver
- To view the home page, go to the url: `http://127.0.0.1:8000`
- To view the about page, go to the url: `http://127.0.0.1:8000/about`