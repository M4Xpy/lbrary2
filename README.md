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
# ###############################################################
same with pycharm
# ##################################################################
new project
django
name of the project

python manage.py startapp catalog
in library/settings.py add "catalog" to INSTALLED_APPS
        TIME_ZONE = "Europe/Kiev"
black library
        git add catalog

create models in models.py
class Author(AbstractUser):
    pass

# in settings.py define default user
AUTH_USER_MODEL = "catalog.Author" 

# in models.py
authors = models.ManyToManyField(AUTH_USER_MODEL, related_name="books")  # not Author
python manage.py makemigrations
python manage.py migrate
db # double click and activate

python manage.py createsuperuser

# ##################################
# Register your models in admin.py
admin.site.register(LiteraryFormat) 

@admin.register(Book)  # admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "format", ]
    list_filter = ["format", ]
    search_fields = ["title", ]

@admin.register(Author)  # admin.site.register(Author, UserAdmin)
class AuthorAdmin(UserAdmin):
    UserAdmin.list_display += ("pseudonym",)
    UserAdmin.fieldsets += (
        ("additional information", {"fields": ("pseudonym",)}),
    )
    UserAdmin.add_fieldsets += (
        ("additional information", {"fields": ("first_name", "last_name", "pseudonym",)}),
    )
# ###########################################
complete django intro 
# ###########################################
# views.py
def home(request: HttpRequest,
         uniq_number: int,
         ) -> HttpResponse:
    print(f"request method: {request.method}\n"
          f"request         {request}\n"
          f"request params  {request.GET}")
    return HttpResponse("<h1>Hello World!</h1>"

                        f"<h4>Unique number is {uniq_number}</h4>")
# urls.py
add path("home/<int:uniq_number>/", home, ), to urlpatterns
path("", include("catalog.urls"), )

    http://localhost:8000/home/22/?param1=asdf
request params  <QueryDict: {'param1': ['asdf']}>

create app's catalog/urls.py
urlpatterns = [
    path('', index, name="index"),
]

in main-project library/urls.py
urlpatterns = [
    path("", include("catalog.urls"), ),

# library/urls.py
path("catalog/", include("catalog.urls", namespace="catalog"), )
]
# catalog/urls.py
app_name = 'catalog'

create folder catalog in templates
create index.html in catalog 

# catalog/admin.py
def index(request: HttpRequest) -> HttpResponse:
    return render(request,
                  "catalog/index.html",
                  {"formats": LiteraryFormat.objects.count(), })
in html           <li>Literary formats: {{ formats }}</li>

# bootstrap  add in head
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
        integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
download library by prompt

# inherit  from base-template
{% extends "base.html" %}

# to change value
{% block title %}
  <title>Home page</title>
{% endblock title %}

# to able part of html from includes/sidebar.html
    {% block sidebar %}
      {% include "includes/sidebar.html" %}
    {% endblock sidebar %}

# to enable static files
# setting.py
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# warning   after bootsrap-line
<head>
  {% load static %}
  <link rel="stylesheet" href="{% static 'CSS/styles.css' %}">
</head>

# ###########################################
complete mvt
# ###########################################





































