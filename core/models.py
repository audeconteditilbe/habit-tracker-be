from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Habit(models.Model):
    GOAL_TYPE_CHOICES = [
        ("gt", "Greater than"),
        ("gte", "Greater than or equal to"),
        ("lt", "Less than"),
        ("lte", "Less than or equal to"),
        ("equal", "Equal to"),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('deleted', 'Deleted'),
    ]

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="habits"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    private = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default='active', choices=STATUS_CHOICES)
    goalFrequency = models.IntegerField()
    goalTimespan = models.IntegerField(validators=[MinValueValidator(0)])
    goalType = models.CharField(max_length=10, choices=GOAL_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Entry(models.Model):
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name="entries"
    )
    date = models.DateTimeField(auto_now_add=True)
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
