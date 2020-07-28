from django.urls import path

from . import views

urlpatterns = [
    path("", views.conjugate, name="conjugate"),
    path("<int:lang_id>", views.tenses, name="tenses"),
    path("<int:lang_id>/conjugations", views.conjugations, name="conjugations")
]
