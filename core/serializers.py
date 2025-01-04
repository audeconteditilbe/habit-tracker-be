from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Entry, Habit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

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
            "goal",
            "goalType",
            "goalTimespan",
            "goalFrom",
            "goalTo",
        ]

    def validate(self, data: dict):
        goalFrom = data.get("goalFrom")
        goalTo = data.get("goalTo")

        if goalFrom and goalTo and goalFrom >= goalTo:
            raise serializers.ValidationError(
                {"goalTo": "finish must occur after start"}
            )

        return data


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["id", "habit", "date", "rating", "description"]
