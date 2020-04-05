from library_app.models import Book, Magazine
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    books = Book.objects.filter(is_available=True)
    magazines = Magazine.objects.filter(is_available=True)
    context = {"books": books, "magazines": magazines}

    return render(request, "library_app/index.html", context)
