# SimpleDjangoReg

A simple Django based registration application for a coding interview. The application is persiting in SQLite database. 

This is a Django site built using Django 2. The following is a quick rundown of how to get started using the data available so far. This documentation assumes the following of whoever reads it:
- Understands Python 2 and 3 principles
- Has some knowledge of Django 1 and 2.
- Is comfortable using Unix terminals

The documentation below does not cover tutorials for the following:
- GIT
- Django 2
- Python 3
- Python virtual environments

Required to run package:
- Python 3
- Git CLI
- A copy of the repo. Get it using: git clone https://github.com/Kayt/SimpleDjangoReg.git
- The database. You could just migrate and create a new one.

### Installation
Install GIT for your platform then:
> git clone https://github.com/Kayt/SimpleDjangoReg.git

> cd SimpleDjangoReg


Install Python 3 and install virtualenv package. Once that's done create a virtual env in the SimpleDjangoFolder folder.
> virtualenv venv

Activate virtualenv using platform specific format (windows format shown below)
> source venv/bin/activate

Once virtual env has been activated, install packages into env
> pip install -r requirements.txt

One more thing, create your database by running migrations, the following command will create the database automatically
> python manage.py makemigrations
> python manage.py migrate

Setup done. Run server using:
> python manage.py runserver

### Enjoy!!!