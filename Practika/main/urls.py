from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", index, name="index"),
    path("test1", views.test1, name="test1"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
]
