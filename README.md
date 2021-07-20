# simple-web-django
website sederhana yang dibuat dengan django + bootstrap

### Run

1. membuat  venv

```
pip install -r requirements.txt --no-cache-dir --upgrade pip
```
### Upgrade Database

```bash
python manage.py makemigrations python manage.py migrate 
```

### Membuat User

```bash
python manage.py createsuperuser --email=admin@django.id --username=admin
```

```bash
python manage.py runserver
```
