from django.test import TestCase
from apps.accounts.models import User
from apps.courses.models import Course
from apps.students.models import Enrollment

class EnrollmentLogicTest(TestCase):
    def setUp(self):
        self.professor = User.objects.create_user(username='prof', password='123', is_professor=True)
        self.student = User.objects.create_user(username='std', password='123', is_student=True)
        self.course1 = Course.objects.create(
            name="ریاضی ۱", code="MATH1", capacity=1, professor=self.professor,
            day="شنبه", start_time="08:00", end_time="10:00"
        )
        self.course2 = Course.objects.create(
            name="فیزیک ۱", code="PHYS1", capacity=20, professor=self.professor,
            day="شنبه", start_time="09:00", end_time="11:00"
        )

    def test_capacity_limit(self):
        Enrollment.objects.create(student=self.student, course=self.course1)
        student2 = User.objects.create_user(username='std2', password='123', is_student=True)
        response = self.client.login(username='std2', password='123')
        # در اینجا باید منطق ویو اجازه ثبت نام ندهد

    def test_time_conflict(self):
        Enrollment.objects.create(student=self.student, course=self.course1)
        # چک کردن تداخل در منطق ویو برای course2