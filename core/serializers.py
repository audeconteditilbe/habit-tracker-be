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
            "author",
            "name",
            "description",
            "private",
            "status",
            "goalFrequency",
            "goalTimespan",
            "goalType",
        ]

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["id", "habit", "date", "rating", "description"]
