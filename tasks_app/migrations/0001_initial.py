# Generated by Django 4.1.7 on 2023-03-21 15:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tile",
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
                ("launch_date", models.DateField(default=django.utils.timezone.now)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("live", "Live"),
                            ("pending", "Pending"),
                            ("archived", "Archived"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=255)),
                ("order", models.PositiveIntegerField()),
                ("description", models.TextField()),
                (
                    "task_type",
                    models.CharField(
                        choices=[
                            ("survey", "Survey"),
                            ("discussion", "Discussion"),
                            ("diary", "Diary"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "tile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="tasks_app.tile",
                    ),
                ),
            ],
        ),
    ]
