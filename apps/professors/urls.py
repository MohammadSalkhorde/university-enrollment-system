from django.urls import path
from . import views

app_name = 'professors'

urlpatterns = [
    path('my-courses/', views.my_teaching_courses, name='my_courses'),
    path('course/<int:course_id>/students/', views.enrolled_students, name='student_list'),
    
    path('course/remove-student/<int:enrollment_id>/', views.remove_student_by_professor, name='remove_student'),
]