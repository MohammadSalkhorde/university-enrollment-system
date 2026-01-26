from django.db import models
from apps.accounts.models import User
from apps.courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments', verbose_name="دانشجو")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_students', verbose_name="درس")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت‌نام")
    is_passed = models.BooleanField(default=False, verbose_name="پاس شده")
    term = models.CharField(max_length=10, default="1402-2", verbose_name="ترم")

    class Meta:
        unique_together = ('student', 'course', 'term')
        verbose_name = "انتخاب واحد"
        verbose_name_plural = "لیست انتخاب واحد"

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.course.name}"