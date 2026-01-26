from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    identification_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.username} - {self.get_full_name()}"