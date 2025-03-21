# Generated by Django 5.1.4 on 2025-01-03 23:28

import graphene.types.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_habit_options_alter_habit_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="status",
            field=models.CharField(
                choices=[
                    (graphene.types.enum.HabitStatus["ACTIVE"], "Active"),
                    (graphene.types.enum.HabitStatus["PAUSED"], "Paused"),
                    (graphene.types.enum.HabitStatus["DELETED"], "Deleted"),
                ],
                default="active",
                max_length=10,
            ),
        ),
    ]
