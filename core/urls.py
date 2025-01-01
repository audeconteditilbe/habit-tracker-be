from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView
from .views import HabitListCreate, HabitDetail, EntryListCreate, EntryDetail, summary_view

urlpatterns = [
    path("habits", HabitListCreate.as_view(), name="habits"),
    path("habits/<int:pk>/", HabitDetail.as_view(), name="habit-detail"),
    path("entries", EntryListCreate.as_view(), name="entries"),
    path("entries/<int:pk>", EntryDetail.as_view(), name="entry-detail"),
    path("gql/summary", summary_view()),
    path("gql/graphql-tool", GraphQLView.as_view(graphiql=True)),
]

# TODO: find out what this does :)
format_suffix_patterns(urlpatterns)
