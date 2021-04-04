from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resources", views.resources, name="resources"),
    path("references", views.references, name="references"),
    path("contact", views.contact, name="contact"),
    path("roadmap", views.roadmap, name="roadmap")
]
