from django.db import models
from django.conf import settings
from apps.courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_student': True},
        related_name='enrollments'
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_students')
    is_passed = models.BooleanField(default=False)
    term = models.CharField(max_length=10, default="1402-2")

    class Meta:
        unique_together = ('student', 'course', 'term')