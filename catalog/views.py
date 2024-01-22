import datetime
from urllib.request import Request

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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