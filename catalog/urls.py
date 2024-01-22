from django.urls import path

from catalog.views import (index,
                           home,
                           LiteraryFormatListView,
                           BookListView,
                           book_detail_view,
                           BookDetailView,
                           AuthorListView,
                           )

urlpatterns = [
    path('', index, name="index"),
    path("home/", home, ),
    path('literary-formats/',
         LiteraryFormatListView.as_view(),
         name="literary-formats-list"),
    path('books/',
         BookListView.as_view(),
         name="book-list"),
    path('books/<int:pk>/',
         BookDetailView.as_view(),
         name="book-detail"),
    path('authors/',
         AuthorListView.as_view(),
         name="author-list"),
]

app_name = 'catalog'
