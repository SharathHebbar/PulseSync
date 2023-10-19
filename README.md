# PulseSync

A place to store all your reference Links

## To run this application

- pip install -r requirements.txt
- python manage.py runserver
- Navigate to http://127.0.0.1:8000/

## To build this application

- Create a Venv
    - python -m venv venv

- Activate Venv
    - venv\Scripts\activate    

- Install Django
    - pip install django

- Create Django Project
    - django-admin startproject pulsesync
    - cd pulsesync

- Create app for base pages
    - python manage.py startapp core
    - python manage.py runserver

- Create some templates, views
    - Create templates then add that to views.py in app and urls.py in app (app here refers to core)
    - Include the urls of the app to the urls.py of main (main here refers to pulsesync)

- Implement Tailwind CSS
    - Used tailwind as a script

- Create app for users
    - python manage.py startapp accounts
    - python manage.py makemigrations
    - python manage.py migrate

- Set up authentication
    - Sign up
    - Log In
    - Log Out

- Create app for links
    - python manage.py startapp links
    - Models for link and categories
    - Views

- Create app for Dashboard
    - python manage.py startapp dashboard

- Category List Page
    - Edit Category
    - Delete Category

- Links
    - Edit Link
    - Delete Link

- Add Category filter on the links page

- Implement Limitations

- Implement a payment gateway (dj-stripe)
    - pip install dj-stripe
    - python manage.py migrate
    - python manage.py djstripe_sync_plans_from_stripe
