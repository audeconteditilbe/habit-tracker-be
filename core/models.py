from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Habit(models.Model):
    UNIT_CHOICES = [
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year'),
    ]

    GOAL_TYPE_CHOICES = [
        ('gt', 'Greater than'),
        ('gte', 'Greater than or equal to'),
        ('lt', 'Less than'),
        ('lte', 'Less than or equal to'),
        ('equal', 'Equal to'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    goal_frequency = models.IntegerField()
    goal_unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    goal_type = models.CharField(max_length=10, choices=GOAL_TYPE_CHOICES)

    def __str__(self):
        return self.name

class Entry(models.Model):
    habit_id = models.ForeignKey(Habit, on_delete=models.CASCADE)
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
        return f"{self.date}_{self.habit_id}"
