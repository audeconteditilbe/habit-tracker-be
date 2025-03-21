from datetime import datetime

from django.http import Http404
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view

from graphene_django.views import GraphQLView

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from .types import EntryListQuery, HabitListQuery
from .models import Entry, Habit, HabitStatus
from .serializers import (
    CreateUserSerializer,
    EntrySerializer,
    HabitSerializer,
    UserSerializer,
)


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(request, pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        try:
            return User.objects.get(pk=request.user.id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object(request)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                name="userId",
                description="Filter habits by the author's user ID.",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="status",
                description="Filter by status",
                required=False,
                type=str,
                enum=(
                    HabitStatus.ACTIVE.value,
                    HabitStatus.PAUSED.value,
                    HabitStatus.DELETED.value,
                ),
            ),
            OpenApiParameter(
                name="ongoing",
                description="Include only ongoing habits. Defaults to 1 (true).",
                required=False,
                type=str,
                enum=("0", "1"),
            ),
        ],
        description="Retrieve a list of habits.",
    ),
    post=extend_schema(
        description="Create a new habit.",
    ),
)
class HabitListCreate(ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method != "GET":
            return Habit.objects.all()
        query: HabitListQuery = self.request.GET
        author = query.get("userId")
        status = query.get("status")

        habits = Habit.objects.filter(author=author).filter(status=status)

        if self.request.user.id != author:
            habits = habits.filter(private=False)

        ongoing_only = query.get("ongoing") == "1"
        if ongoing_only:
            now = datetime.now()
            habits = habits.filter(
                Q(goalFrom__isnull=True) | Q(goalFrom__gte=now)
            ).filter(Q(goalTo__isnull=True) | Q(goalTo__lte=now))

        return habits


class HabitDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            habit = Habit.objects.get(pk=pk)
            print(habit.author != self.request.user.id and habit.private)
            if habit.author != self.request.user.id and habit.private:
                raise Http404

            return Response(HabitSerializer(habit).data)
        except Habit.DoesNotExist:
            raise Http404


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                name="habitId",
                description="Filter entries by the habit ID",
                required=True,
                type=str,
            ),
            OpenApiParameter(
                name="timeStart",
                description="Start date for filtering entries in ISO format."
                + " Defaults to 7 days before `timeEnd`.",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="timeEnd",
                description="End date for filtering entries in ISO format."
                + " Defaults to the current time.",
                required=False,
                type=str,
            ),
        ],
        description="Retrieve entries filtered by habit and date range.",
    ),
    post=extend_schema(
        description="Create a new entry for a habit.",
    ),
)
class EntryListCreate(ListCreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method != "GET":
            return Entry.objects.all()

        query: EntryListQuery = self.request.GET

        habitId = query.get("habitId")

        if not habitId:
            raise Http404

        end = query.get("timeEnd")
        start = query.get("timeStart")

        if end and start:
            start = datetime.fromisoformat(start)
            end = datetime.fromisoformat(end)
            return (
                Entry.objects.filter(habit=habitId)
                .filter(date__date__range=(start, end))
                .order_by("-date")
            )
        if start:
            start = datetime.fromisoformat(start)
            return (
                Entry.objects.filter(habit=habitId)
                .filter(date__date__gt=start)
                .order_by("-date")
            )
        if end:
            end = datetime.fromisoformat(end)
            return (
                Entry.objects.filter(habit=habitId)
                .filter(date__date__lt=end)
                .order_by("-date")
            )

        return Entry.objects.filter(habit=habitId).order_by("-date")


class EntryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            return Response(EntrySerializer(Entry.objects.get(pk=pk)).data)
        except Entry.DoesNotExist:
            raise Http404


def summary_view():
    """
    Wrapper for GraphQLView to enforce authentication
    through recycling of DRF simple JWT auth
    https://github.com/graphql-python/graphene/issues/249
    """
    view = GraphQLView.as_view()
    view = permission_classes((IsAuthenticated,))(view)
    # view = authentication_classes((TokenAuthentication,))(view)
    view = api_view(["GET", "POST"])(view)
    return view
