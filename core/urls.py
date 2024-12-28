from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("habits", views.HabitListCreate.as_view(), name="habits"),
    path("habits/<int:pk>/", views.HabitDetail.as_view(), name="habit-detail"),
    path("entries", views.EntryListCreate.as_view(), name="entries"),
    path("entries/<int:pk>", views.EntryDetail.as_view(), name="entry-detail"),
]

# TODO: find out what this does :)
format_suffix_patterns(urlpatterns)
