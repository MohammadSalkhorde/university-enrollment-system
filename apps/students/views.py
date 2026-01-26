from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.courses.models import Course
from apps.core.logic import EnrollmentValidator
from .models import Enrollment

def student_dashboard(request):
    courses = Course.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        courses = courses.filter(name__icontains=search_query) | courses.filter(professor__last_name__icontains=search_query)
    return render(request, 'students/course_list.html', {'courses': courses})

def enroll_action(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    is_valid, error_msg = EnrollmentValidator.validate(request.user, course)
    if is_valid:
        Enrollment.objects.create(student=request.user, course=course, term="1402-2")
        messages.success(request, "درس با موفقیت اخذ شد.")
    else:
        messages.error(request, error_msg)
    return redirect('students:dashboard')

def weekly_schedule(request):
    enrollments = Enrollment.objects.filter(student=request.user, term="1402-2")
    return render(request, 'students/schedule.html', {'enrollments': enrollments})

def drop_unit(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user, term="1402-2")
    enrollment.delete()
    messages.success(request, "درس حذف شد.")
    return redirect('students:schedule')