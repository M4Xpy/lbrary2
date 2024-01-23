import datetime
from urllib.request import Request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = -~num_visits

    return render(request,
                  "catalog/index.html",
                  {"num_books": Book.objects.count(),
                   "num_authors": Author.objects.count(),
                   "formats": LiteraryFormat.objects.count(),
                   "num_visits": num_visits + 1,
                   }
                  )


class LiteraryFormatListView(LoginRequiredMixin, ListView):
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


def test_session_view(request: HttpRequest,
                      ) -> HttpResponse:
    request.session["book"] = "Test Session book"
    return HttpResponse("<h1>Test Session</h1>"
                        f"<h4>Session data: {request.session['book']}</h4>")
