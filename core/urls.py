from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HabitListCreate, HabitDetail, EntryListCreate, EntryDetail

urlpatterns = [
    path("habits", HabitListCreate.as_view(), name="habits"),
    path("habits/<int:pk>/", HabitDetail.as_view(), name="habit-detail"),
    path("entries", EntryListCreate.as_view(), name="entries"),
    path("entries/<int:pk>", EntryDetail.as_view(), name="entry-detail"),
]

# TODO: find out what this does :)
format_suffix_patterns(urlpatterns)
