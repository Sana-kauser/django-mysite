# from django.contrib import admin
from django.urls import path
# import views from current directory
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view1"),
    path("v2/", views.v2, name="view2"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),
    # path("index/", views.v2, name="index"),
]
