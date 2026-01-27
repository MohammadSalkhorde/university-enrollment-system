from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # path('dashboard/', views.student_dashboard, name='dashboard'),
    # path('enroll/<int:course_id>/', views.enroll_course, name='enroll'),
    # path('drop/<int:enrollment_id>/', views.drop_course, name='drop'),
    # path('schedule/', views.student_dashboard, name='schedule'), 
    path('dashboard/', views.student_dashboard, name='dashboard'),
]