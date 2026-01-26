from django.db import models
from apps.accounts.models import User
from apps.courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_students')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_passed = models.BooleanField(default=False)
    term = models.CharField(max_length=10, default="1402-2")

    class Meta:
        unique_together = ('student', 'course', 'term')

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.course.name}"