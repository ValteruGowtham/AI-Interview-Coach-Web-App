from django.urls import path
from . import views

app_name = "interview"

urlpatterns = [
    path("", views.home, name="home"),
    path("simulate/", views.simulate, name="simulate"),
]
