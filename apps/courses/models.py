from django.db import models
from django.conf import settings
from apps.accounts.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    professor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_professor': True})
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name

class SystemSetting(models.Model):
    min_units = models.PositiveIntegerField(default=12)
    max_units = models.PositiveIntegerField(default=20)