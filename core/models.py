from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from graphene import Enum


class HabitStatus(Enum):
    ACTIVE = '0'
    PAUSED = '1'
    DELETED = '2'


class Habit(models.Model):
    class Meta:
        ordering = ["private", "status", "goalFrom", "goalTimespan"]

    GOAL_TYPE_CHOICES = [
        ("GT", "Greater than"),
        ("GTE", "Greater than or equal to"),
        ("LT", "Less than"),
        ("LTE", "Less than or equal to"),
        ("EQUAL", "Equal to"),
    ]

    STATUS_CHOICES = [
        (HabitStatus.ACTIVE.value, "Active"),
        (HabitStatus.PAUSED.value, "Paused"),
        (HabitStatus.DELETED.value, "Deleted"),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    private = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default="active", choices=STATUS_CHOICES)
    goal = models.IntegerField(blank=True, null=True)
    goalType = models.CharField(
        max_length=10, choices=GOAL_TYPE_CHOICES, blank=True, null=True
    )
    goalTimespan = models.IntegerField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    goalFrom = models.DateTimeField(blank=True, null=True)
    goalTo = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="entries")
    date = models.DateTimeField()
    rating = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date}_{self.habit}"
