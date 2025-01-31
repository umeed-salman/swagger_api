# Generated by Django 4.2.16 on 2024-10-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day_of_week", models.CharField(max_length=10)),
                ("start_time", models.TimeField()),
                ("stop_time", models.TimeField()),
                ("ids", models.JSONField()),
            ],
            options={"unique_together": {("day_of_week", "start_time", "stop_time")},},
        ),
    ]
