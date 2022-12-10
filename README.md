# feednews

feednews is a web-based RSS feed reader with filtering and search capability

## Installation
you need python3 and pip for install requirements after get project with git clone

```python
pip install -r requirements.txt
```

next step

```python
python manage.py makemigrations && python manage.py migrate
```

now you should create superuser for admin

```python
python manage.py createsuperuser
```

now you can run server and use this website
```python
python manage.py runserver
```

You should go to `admin/`, sign in with your superuser that you create before then add agency. 
Open `update/` click on post now go `feed/` and see results