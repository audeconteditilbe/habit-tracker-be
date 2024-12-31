from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView
from .views import HabitListCreate, HabitDetail, EntryListCreate, EntryDetail

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view

# Recycle DRF simple JWT auth for Graphene-Django
# https://github.com/graphql-python/graphene/issues/249
def graphql_token_view():
    view = GraphQLView.as_view()
    view = permission_classes((IsAuthenticated,))(view)
    # view = authentication_classes((TokenAuthentication,))(view)
    view = api_view(['GET', 'POST'])(view)
    return view

urlpatterns = [
    path("habits", HabitListCreate.as_view(), name="habits"),
    path("habits/<int:pk>/", HabitDetail.as_view(), name="habit-detail"),
    path("entries", EntryListCreate.as_view(), name="entries"),
    path("entries/<int:pk>", EntryDetail.as_view(), name="entry-detail"),
    path("summary", graphql_token_view()),
    path("graphql-tool", GraphQLView.as_view(graphiql=True)),
]

# TODO: find out what this does :)
format_suffix_patterns(urlpatterns)
