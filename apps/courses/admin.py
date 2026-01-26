from django.contrib import admin
from .models import Course, SystemSetting

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'professor', 'capacity', 'get_enrolled_count', 'day', 'start_time')
    search_fields = ('name', 'code', 'professor__last_name')
    list_filter = ('day', 'professor')
    filter_horizontal = ('prerequisites',)

    def get_enrolled_count(self, obj):
        return obj.enrolled_students.count()
    get_enrolled_count.short_description = 'تعداد ثبت‌نامی'

@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('min_units', 'max_units')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)