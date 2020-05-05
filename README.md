# python

To run/modify employados:


python3 -m venv tutorial-env

source /tutorial-env/bin/activate

Python 3.8.1

pip install Django

# To create the project:
django-admin.py startproject learning_log .

# Create database:
python manage.py migrate

# Run Server:
python manage.py runserver
