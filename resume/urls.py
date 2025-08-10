from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_resume, name="upload_resume"),
]
