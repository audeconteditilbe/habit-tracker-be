# Generated by Django 5.1.4 on 2024-12-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_habit_author_entry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
