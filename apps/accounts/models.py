from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=150, verbose_name="نام")
    last_name = models.CharField(max_length=150, verbose_name="نام خانوادگی")
    
    student_id = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="کد دانشجویی")
    professor_id = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="کد استادی")
    
    is_student = models.BooleanField(default=False, verbose_name="دانشجو")
    is_professor = models.BooleanField(default=False, verbose_name="استاد")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"