from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.author}"


class BookLoan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loaned_timestamp = models.DateTimeField(auto_now_add=True)
    returned_timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"
