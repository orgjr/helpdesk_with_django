## A simple helpdesk system with Django deployed on a local server.

### Run the project

#### 📦 Software Requirements

- **Python 3.8+**
    
- **pip** (Python's packet manager)
    
- **git**

```
git clone https://github.com/orgjr/helpdesk_with_django.git

cd helpdesk_with_django

python3 -m venv venv

source venv/bin/activate

pip install django

pip install material

pip install django.material

pip install django_widget_tweaks

python3 manage.py runserver 127.0.0.1:8080
```

Access http://127.0.0.1:8080 in a web browser


default admin
```
user: admin
password: 123
```

create super user
```
python3 manager.py createsuperuser
```

to full admin functions mark user as_operador and as_admin

access http://127.0.0.1:8080/admin