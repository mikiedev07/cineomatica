# Cineomatica

A project representing work with the API of a cinema site for booking and watching available movies

## Getting Started

### Prerequisites

To run the project You need Python 3+ version to be installed on your computer. 
To check your Python Version on Windows in console:
```
python -V
```

### Installing

Also, you need to install some python libraries like Django, Rest Framework etc.
You can install it by using requirements file in root directory by command (on Windows):

```
pip install -r /path/to/requirements.txt
```

To check if you did install correctly, get to root directory (with manage.py file) and type in console:

```
python manage.py runsever [8001]
```

This will run local server (Port optional).

## Authentication

The site is equipped with JWT authentication, so you will need to use Bearer tokens to use the full functionality of the site.

## API docs

To check Swagger documentation go to http://host:port/ (home page).