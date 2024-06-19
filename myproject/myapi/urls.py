from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login-view"),
    path("register/", views.register, name="register"),
]


# api-endpoint urls