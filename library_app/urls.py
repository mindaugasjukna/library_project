from django.urls import path
from . import views

app_name = "library_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("loan/<str:type>/<int:id>", views.loan_item, name="loan_item"),
]
