# Generated by Django 5.1.4 on 2024-12-31 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_habit_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="goal_unit",
        ),
        migrations.AddField(
            model_name="habit",
            name="goal_timespan",
            field=models.IntegerField(
                default=7, validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
    ]
