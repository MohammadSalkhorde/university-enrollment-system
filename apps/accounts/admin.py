from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'student_id', 'professor_id', 'is_student', 'is_professor', 'is_staff')
    
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات نقش کاربر', {'fields': ('is_student', 'is_professor', 'student_id', 'professor_id')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('اطلاعات نقش کاربر', {'fields': ('is_student', 'is_professor', 'student_id', 'professor_id')}),
    )

