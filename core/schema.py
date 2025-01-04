from datetime import datetime
import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from core.utils import days_ago
from .models import Habit, Entry, HabitStatus


class EntryType(DjangoObjectType):
    class Meta:
        model = Entry
        fields = ("id", "habit", "date", "rating", "description")


class HabitType(DjangoObjectType):
    class Meta:
        model = Habit
        fields = (
            "id",
            "author",
            "name",
            "description",
            "private",
            "status",
            "goal",
            "goalType",
            "goalTimespan",
            "goalFrom",
            "goalTo",
        )

    entries = graphene.List(EntryType, span=graphene.Int(required=False))

    def resolve_entries(self: Habit, info, days=10):
        return (
            Entry.objects.filter(habit=self)
            .filter(date__gt=days_ago(days))
            .order_by("-date")
        )


class Query(graphene.ObjectType):
    habits = graphene.List(HabitType, author=graphene.Int(required=True))

    def resolve_habits(self, info, author):
        """
        Gets habits of selected user, that are active and currently ongoing (goal range
        is not set outside of today). If the requesting user is not the same as author,
        private habits are not returned.
        """
        now = datetime.now()
        userId: str = info.context.user.id

        habits = (
            Habit.objects.filter(author=author)
            .filter(status=HabitStatus.ACTIVE.value)
            .filter(Q(goalFrom__isnull=True) | Q(goalFrom__lte=now))
            .filter(Q(goalTo__isnull=True) | Q(goalTo__gte=now))
        )

        if userId != author:
            habits = habits.filter(private=False)

        return habits


schema = graphene.Schema(query=Query)
