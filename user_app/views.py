from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as dj_login
from django.http import HttpResponseRedirect
from library_app.models import Book, BookLoan


def login(request):
    context = {}

    # LOGIN
    if request.method == "POST":
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])

        if user:
            # Succesful login
            dj_login(request, user)
            return HttpResponseRedirect(reverse("library_app:index"))

        else:
            # Failed login
            context = {"error_message": "Invalid username or password"}

    return render(request, "user_app/login.html", context)
