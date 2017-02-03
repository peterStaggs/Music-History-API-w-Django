<h2>Music History Django API</h2>

This is a simple API built with Django for accessing information on songs, albums, artists, and genres. API users can quickly post these items to a persistent database.   

Initial Setup

Install Python 3.6
Install Pip
Getting Started

Using your terminal:

pip install django
pip install djangorestframework
After installing django, djangorestframework, and pygments, clone the repo locally to your computer.

Sync the Database

In the main project directory, run:

python manage.py makemigrations 
python manage.py migrate

Run the Server

python manage.py runserver (specify port here if desired)

Check to see where the server is running. (Example: Development server is running at http://127.0.0.1:8000/)

On your browser, go to your local host (Example: http://localhost:8000/)