create project
(
python3.12 -m venv venv
source venv/bin/activate
) 
pip install django   
        django-admin --version
django-admin startproject app . # create app django-project in current project
        python manage.py runserver
        ctrl + c 
        * 
        edit configurations
        +
        django server
        set name (App)
        fix
        enable django support
        choose django project root
        choose settings file
        apply
        ok
        apply
        ok
################################################################
same with pycharm
###################################################################
new project
django
name of the project

python manage.py startapp catalog
in library/settings.py add "catalog" to INSTALLED_APPS
        TIME_ZONE = "Europe/Kiev"
black library

