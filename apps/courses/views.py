from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

def course_list_admin(request):
    courses = Course.objects.all()
    return render(request, 'courses/manage_courses.html', {'courses': courses})

def create_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('courses:manage_list')
    return render(request, 'courses/course_form.html', {'form': form})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('courses:manage_list')
    return render(request, 'courses/course_form.html', {'form': form})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
    return redirect('courses:manage_list')