# Seed
Seed project with startappsimple method.
## Usage
Clone it. Create virtual enviroment, install all requirements, make migrations and run the server. Don't forget to activate the enviroment
```sh
python -m venv env

pip install -r requremets.txt

python manage.py makemigrations users
python manage.py makemigrations posts
python manage.py migrate

python manage.py runserver
```
