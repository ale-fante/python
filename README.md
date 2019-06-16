# python

To run/modify employados:


python -m virtualenv venv

source venv/bin/activate

pip install Django

# To create the project:
django-admin.py startproject learning_log .

# Create database:
python manage.py migrate

# Run Server:
python manage.py runserver