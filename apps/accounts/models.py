from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False, verbose_name="دانشجو")
    is_professor = models.BooleanField(default=False, verbose_name="استاد")
    student_id = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="شماره دانشجویی")
    professor_id = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="کد استادی")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"