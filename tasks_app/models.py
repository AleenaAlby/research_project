from django.db import models
from django.utils import timezone

# Create your models here.

class Tile(models.Model):
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('pending', 'Pending'),
        ('archived', 'Archived'),
    )
    launch_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default ='pending')


class Task(models.Model):
    TYPE_CHOICES = (
            ('survey', 'Survey'),
            ('discussion', 'Discussion'),
            ('diary', 'Diary'),
        )

    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    description = models.TextField()
    task_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, related_name='tasks')