import graphene
from graphene_django import DjangoObjectType
from .models import Habit, Entry

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
            "goal_frequency",
            "goal_timespan",
            "goal_type",
        )

    entries = graphene.List(EntryType, span=graphene.Int(required=False))

    def resolve_entries(self: Habit, info, span = None):
        if not span or span <= 0:
            span = self.goal_timespan if self.goal_timespan > 0 else 7
        
        return Entry.objects.filter(habit=self).order_by('-date')[:span]

class Query(graphene.ObjectType):
    habits = graphene.List(HabitType, author=graphene.Int(required=True))
    
    def resolve_habits(self, info, author):
        return Habit.objects.filter(author=author)

schema = graphene.Schema(query=Query)