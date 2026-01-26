from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_professor': True},
        related_name='taught_courses'
    )
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"

class SystemSetting(models.Model):
    min_units = models.PositiveIntegerField(default=12)
    max_units = models.PositiveIntegerField(default=20)