from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('manage/', views.course_list_admin, name='manage_list'),
    path('create/', views.create_course, name='create'),
    path('edit/<int:course_id>/', views.edit_course, name='edit'),
    path('delete/<int:course_id>/', views.delete_course, name='delete'),
    
    # بخش دانشجو
    path('dashboard/', views.student_dashboard, name='dashboard'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll'), # این خط باید باشه
    path('drop/<int:course_id>/', views.drop_course, name='drop'),
]