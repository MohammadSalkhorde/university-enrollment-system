from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='dashboard'),
    path('enroll/<int:course_id>/', views.enroll_action, name='enroll'),
    path('drop/<int:enrollment_id>/', views.drop_unit, name='drop_unit'),
    path('schedule/', views.weekly_schedule, name='schedule'),
]