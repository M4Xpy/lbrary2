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
        git add catalog

create models in models.py
class Author(AbstractUser):
AUTH_USER_MODEL = "catalog.Author"   # in settings # define default user
authors = models.ManyToManyField(AUTH_USER_MODEL, related_name="books")  # not Author
python manage.py makemigrations
python manage.py migrate
db # double click and activate

python manage.py createsuperuser

# ##################################
admin.site.register(LiteraryFormat) # Register your models in manage.py

@admin.register(Book)  # admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "format", ]
    list_filter = ["format", ]
    search_fields = ["title", ]

@admin.register(Author)  # admin.site.register(Author, UserAdmin)
class AuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("pseudonym",)
    fieldsets = UserAdmin.fieldsets + (
        ("additional information", {"fields": ("pseudonym",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("additional information", {"fields": ("first_name", "last_name", "pseudonym",)}),
    )
# ###########################################
complete django intro 
# ###########################################



































