from django.urls import path

from catalog.views import index, home

urlpatterns = [
    path('', index, name="index"),
    path("home/", home, ),
]

app_name = 'catalog'
