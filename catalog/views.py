import datetime
from urllib.request import Request

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Book, Author, LiteraryFormat


def home(request: HttpRequest,
         uniq_number: int = None,
         ) -> HttpResponse:
    print(f"request method: {request.method}\n"
          f"request         {request}\n"
          f"request params  {request.GET}")
    return HttpResponse("<h1>Hello World!</h1>"
                        f"<h4>Current time is {datetime.datetime.now()}</h4>"
                        f"<h4>Unique number is {uniq_number}</h4>")


def index(request: HttpRequest) -> HttpResponse:
    return render(request,
                  "catalog/index.html",
                  {"num_books": Book.objects.count(),
                   "num_authors": Author.objects.count(),
                   "formats": LiteraryFormat.objects.count(), }
                  )


class LiteraryFormatListView(ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"  # for urls
    context_object_name = "literary_format_list"  # for html


class BookListView(ListView):
    model = Book
    queryset = Book.objects.select_related("format")  # sql-speed improvement
    paginate_by = 10  # pagination   15  books  per  page


class AuthorListView(ListView):
    model = Author


def book_detail_view(request: HttpRequest,
                     pk: int,
                     ) -> HttpResponse:
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404("Book not found")
    return render(request,
                  "catalog/book_detail.html",
                  {"book": book},
                  )


class BookDetailView(DetailView):
    model = Book


