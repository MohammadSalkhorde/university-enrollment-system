from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course, SystemSetting
from .forms import CourseForm

def course_list_admin(request):
    """نمایش لیست دروس و فرم تنظیمات واحدها در یک صفحه"""
    courses = Course.objects.all()
    
    # تلاش برای گرفتن تنظیمات؛ اگر نبود یکی با مقدار پیش‌فرض می‌سازد
    settings, created = SystemSetting.objects.get_or_create(id=1)

    # بررسی ارسال فرم تنظیمات (حداقل و حداکثر واحد)
    if request.method == 'POST' and 'update_settings' in request.POST:
        min_u = request.POST.get('min_units')
        max_u = request.POST.get('max_units')
        
        if min_u and max_u:
            settings.min_units = min_u
            settings.max_units = max_u
            settings.save()
            messages.success(request, "قوانین واحدها با موفقیت به‌روزرسانی شد.")
            return redirect('courses:manage_list')

    # ارسال متغیر settings به قالب
    return render(request, 'courses/manage_courses.html', {
        'courses': courses,
        'settings': settings
    })

def create_course(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "درس جدید با موفقیت ثبت شد.")
        return redirect('courses:manage_list')
    return render(request, 'courses/course_form.html', {'form': form})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, instance=course)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "تغییرات درس ذخیره شد.")
        return redirect('courses:manage_list')
    return render(request, 'courses/course_form.html', {'form': form})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.warning(request, "درس مورد نظر حذف شد.")
    return redirect('courses:manage_list')