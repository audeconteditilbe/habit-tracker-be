# Generated by Django 5.1.4 on 2025-01-03 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_habit_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="goalFrequency",
            new_name="goal",
        ),
    ]
