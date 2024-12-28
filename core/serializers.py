from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Entry, Habit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            "id",
            "name",
            "description",
            "private",
            "goal_frequency",
            "goal_unit",
            "goal_type",
            "author",
        ]
        # uncomment once author will be automatically set to current user
        # extra_kwargs = { "author": { "read_only": True } }


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["id", "habit", "date", "rating", "description"]
