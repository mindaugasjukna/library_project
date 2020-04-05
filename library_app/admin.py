from django.contrib import admin
from .models import Book, BookLoan
# Register your models here.

admin.site.register(Book)
admin.site.register(BookLoan)
