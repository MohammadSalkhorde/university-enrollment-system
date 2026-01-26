from apps.students.models import Enrollment
from apps.courses.models import SystemSetting

class EnrollmentValidator:
    @staticmethod
    def validate(student, course):
        # 1. بررسی تکرار در ترم جاری
        if Enrollment.objects.filter(student=student, course=course, term="1402-2").exists():
            return False, "شما این درس را قبلاً در این ترم اخذ کرده‌اید."

        # 2. بررسی ظرفیت
        enrolled_count = Enrollment.objects.filter(course=course, term="1402-2").count()
        if enrolled_count >= course.capacity:
            return False, "ظرفیت این درس تکمیل شده است."

        # 3. بررسی تداخل زمانی
        current_enrollments = Enrollment.objects.filter(student=student, term="1402-2")
        for enrollment in current_enrollments:
            if enrollment.course.day == course.day:
                # چک کردن تداخل بازه‌های زمانی
                if not (course.end_time <= enrollment.course.start_time or course.start_time >= enrollment.course.end_time):
                    return False, f"تداخل زمانی با درس {enrollment.course.name}."

        # 4. بررسی پیش‌نیاز (باید قبلاً پاس شده باشد)
        for pre in course.prerequisites.all():
            if not Enrollment.objects.filter(student=student, course=pre, is_passed=True).exists():
                return False, f"شما درس پیش‌نیاز {pre.name} را نگذرانده‌اید."

        # 5. بررسی سقف واحد (فرض هر درس 3 واحد)
        settings = SystemSetting.objects.first()
        max_limit = settings.max_units if settings else 20
        if (current_enrollments.count() * 3) + 3 > max_limit:
            return False, "تعداد واحدهای شما از سقف مجاز بیشتر می‌شود."

        return True, None