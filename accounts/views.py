from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# def login_view(request: HttpRequest) -> HttpResponse:
#     if request.method == 'GET':
#         return render(request,
#                       "registration/login.html",
#                       {"error": ""}, )
#     if request.method == 'POST':
#         user = authenticate(username=request.POST['username'],
#                             password=request.POST['password'],
#                             )
#         if user:
#             login(request, user)
#             return HttpResponseRedirect(reverse("catalog:index"))
#         return render(request,
#                       "registration/login.html",
#                       {"error": "Invalid username or password"},
#                       )


# def logout_view(request: HttpRequest) -> HttpResponse:
#     logout(request)
#     return render(request, "registration/logged_out.html")

