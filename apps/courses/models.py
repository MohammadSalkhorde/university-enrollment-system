from django.db import models
from apps.accounts.models import User

class Course(models.Model):
    # تعریف لیست کشویی برای روزهای هفته
    DAYS_OF_WEEK = [
        ('1', 'شنبه'),
        ('2', 'یکشنبه'),
        ('3', 'دوشنبه'),
        ('4', 'سه‌شنبه'),
        ('5', 'چهارشنبه'),
        ('6', 'پنج‌شنبه'),
        ('7', 'جمعه'),
    ]

    name = models.CharField(max_length=100, verbose_name="نام درس")
    code = models.CharField(max_length=20, unique=True, verbose_name="کد درس")
    capacity = models.IntegerField(verbose_name="ظرفیت")
    professor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_professor': True}, 
        verbose_name="استاد"
    )
    # تغییر فیلد روز به انتخاب‌گر (Dropdown)
    day = models.CharField(
        max_length=1, 
        choices=DAYS_OF_WEEK, 
        default='1', 
        verbose_name="روز برگزاری"
    )
    start_time = models.TimeField(verbose_name="زمان شروع")
    end_time = models.TimeField(verbose_name="زمان پایان")
    location = models.CharField(max_length=100, verbose_name="مکان برگزاری")
    prerequisites = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        blank=True, 
        verbose_name="پیش‌نیازها"
    )

    class Meta:
        verbose_name = "درس"
        verbose_name_plural = "دروس"

    def __str__(self):
        return f"{self.name} ({self.get_day_display()})"

class SystemSetting(models.Model):
    min_units = models.PositiveIntegerField(default=12, verbose_name="حداقل واحد")
    max_units = models.PositiveIntegerField(default=20, verbose_name="حداکثر واحد")

    class Meta:
        verbose_name = "تنظیمات سیستم"
        verbose_name_plural = "تنظیمات سیستم"