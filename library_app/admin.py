from django.contrib import admin
from .models import Book, BookLoan, Magazine, MagazineLoan
# Register your models here.

admin.site.register(Book)
admin.site.register(BookLoan)
admin.site.register(Magazine)
admin.site.register(MagazineLoan)
