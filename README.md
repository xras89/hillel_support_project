# About

This is the educational project for IT Hillel

# `pipenv` usage

The pipenv is used as a main package manager on the project. For more information please follow the [🔗 documentation](https://pipenv.pypa.io/en/latest/)

```sh
# Creating a new virtual environment
pipenv shell

# Creating a .lock file from Pipenv file
pipenv lock

# Installing dependencies from .lock file
pipenv sync

# Django startproject
django-admin startproject support

# Django start server
python support/manage.py runserver  

# Sync DEV
pipenv sync --dev

# Sync
pipenv sync

# Clear caches
pipenv --clear
```

