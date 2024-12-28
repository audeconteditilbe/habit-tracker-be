from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("habits", views.HabitListCreate.as_view()),
    path("entries", views.entries_handler, name="entries"),
]

# TODO: find out what this does :)
format_suffix_patterns(urlpatterns)
