from django.db import models

# TODO use Django default User
# class User(models.Model):
#     id = models.CharField(max_length=255, primary_key=True)
#     name = models.CharField(max_length=255)
#     bio = models.TextField(blank=True, null=True)

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

    id = models.CharField(max_length=255, primary_key=True)
    # # TODO
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Goal-related fields
    goal_frequency = models.IntegerField()
    goal_unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    goal_type = models.CharField(max_length=10, choices=GOAL_TYPE_CHOICES)

# class Entry:
#     id = models.CharField(max_length=255, primary_key=True)
#     # TODO
#     habit_id = models.ForeignKey(Habit, on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     # TODO min=0, max=10
#     rating = models.IntegerField()
#     description = models.TextField(blank=True, null=True)
