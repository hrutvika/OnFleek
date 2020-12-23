from django.urls import path

from . import views


urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name = "logout"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("welcome", views.welcome, name="welcome"),
    path("appointment", views.appointment, name="appointment"),
    path("beautify", views.beautify, name="beautify"),
]