# SETUP GUIDE FOR LOCAL TESTING
For this project to function properly

### PYTHON
```bash python```
should give a response  of 
```bash
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

## Django
```bash
pip install django
```

## Django RestFramework
Its advisable to first create a virtual machine to avoid modules being in your local pc for syorage issues.

### Virtual Machine Creation
inside this repo;
```bash
python -m venv <venv_name>
```
and then activate the venv
```bash
<venv_name>\Scripts\activate
```
You should see a ```venv_name``` prefix in the terminal, there are others ways to create a virtual env but this is how one of the way i choose

### INstalling Django RestFramework
```bash 
pip install djangorestframework
```

### ENV LOADER
For loading the content of the enviromental file into memeory
```bash
pip install dotenv
```

### SETTING UP THE PORT
run 
```terminal
python manage.py migrate
```
to create the local database or use the one i attached to this repo(if seen)

and then 
```terminal
python manage.py runserver 8000
```

you can change the 8000 to any number its just a port

access the api at http://localhost:8000/

#### last updated: 16 Aug , 2026 -14:57