from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, SystemSetting
from .forms import CourseForm
from apps.students.models import Enrollment  # ایمپورت مدل واسطه

# --- بخش مدیریت (Admin) ---

def course_list_admin(request):
    courses = Course.objects.all()
    settings, created = SystemSetting.objects.get_or_create(id=1)
    if request.method == 'POST' and 'update_settings' in request.POST:
        min_u = request.POST.get('min_units')
        max_u = request.POST.get('max_units')
        if min_u and max_u:
            settings.min_units = min_u
            settings.max_units = max_u
            settings.save()
            messages.success(request, "قوانین واحدها با موفقیت به‌روزرسانی شد.")
            return redirect('courses:manage_list')
    return render(request, 'courses/manage_courses.html', {'courses': courses, 'settings': settings})

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


# --- بخش دانشجو (Student) ---

@login_required
def student_dashboard(request):
    my_custom_days = [
        ('1', 'شنبه'), ('2', 'یکشنبه'), ('3', 'دوشنبه'),
        ('4', 'سه‌شنبه'), ('5', 'چهارشنبه'), ('6', 'پنج‌شنبه'),
    ]
    
    # ۱. گرفتن تمام رکوردهای ثبت‌نام این دانشجو
    user_enrollments = Enrollment.objects.filter(student=request.user)
    
    # ۲. استخراج درس‌ها برای نمایش در جدول و برنامه هفتگی
    enrolled_courses = [e.course for e in user_enrollments]
    
    # ۳. گرفتن ID درس‌ها برای چک کردن وضعیت (اخذ شده/نشده) در تمپلیت
    enrolled_ids = user_enrollments.values_list('course_id', flat=True)

    # ۴. مدیریت جستجو و نمایش لیست کل دروس
    query = request.GET.get('q')
    all_courses = Course.objects.all()
    if query:
        all_courses = all_courses.filter(name__icontains=query)

    context = {
        'my_custom_days': my_custom_days,
        'enrolled_courses': enrolled_courses,
        'enrolled_ids': enrolled_ids,
        'all_courses': all_courses,
    }
    return render(request, 'students/dashboard.html', context)

@login_required
def enroll_course(request, course_id):
    """تابع اخذ واحد: ایجاد یک رکورد در جدول Enrollment"""
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        
        # بررسی اینکه دانشجو قبلاً این درس را اخذ نکرده باشد
        already_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
        
        if already_enrolled:
            messages.info(request, "این درس قبلاً در لیست شما موجود است.")
        elif Enrollment.objects.filter(course=course).count() >= course.capacity:
            messages.error(request, "ظرفیت این درس تکمیل شده است.")
        else:
            # ایجاد رکورد جدید (ترم را می‌توانید داینامیک کنید)
            Enrollment.objects.create(student=request.user, course=course, term="1402-2")
            messages.success(request, f"درس {course.name} با موفقیت اخذ شد.")
            
    return redirect('courses:dashboard')

@login_required
def drop_course(request, course_id):
    """تابع حذف واحد: پاک کردن رکورد از جدول Enrollment"""
    if request.method == 'POST':
        enrollment = Enrollment.objects.filter(student=request.user, course_id=course_id).first()
        if enrollment:
            enrollment.delete()
            messages.warning(request, "درس با موفقیت از لیست شما حذف شد.")
        else:
            messages.error(request, "خطایی رخ داد؛ درس یافت نشد.")
            
    return redirect('courses:dashboard')