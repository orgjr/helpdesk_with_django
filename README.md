## A simple helpdesk system with Django deployed on a local server.

### Run the project

#### 📦 Software Requirements

- **Python 3.8+**
    
- **pip** (Python's packet manager)
    
- **git**

```
git clone https://github.com/orgjr/helpdesk_with_django.git

cd helpdesk_with_django

py -m venv venv 

.\venv\Scripts\activate

py -m pip install -r requirements.txt

python3 manage.py runserver 127.0.0.1:8080
```

Access http://127.0.0.1:8080 in a web browser

## User Access Levels

### The system has three types of access: **Administrator**, **Operator**, and **User**.

- **Administrator**: Manages system access, adds and configures users.  
- **Operator**: Provides technical support to Users.  
- **User**: Regular system users, such as employees of a company.

A single account can combine the roles of **Administrator** and **Operator**.



### default admin
```
user: admin
password: 123
```

### create super user
```
python3 manager.py createsuperuser
```

to full admin functions mark user is_operador and is_admin

access http://127.0.0.1:8080/admin
