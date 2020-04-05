from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path("", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("loan/<str:type>/<int:id>", views.loan_item, name="loan_item"),
    path("return/<str:type>/<int:id>", views.return_item, name="return_item")
]
