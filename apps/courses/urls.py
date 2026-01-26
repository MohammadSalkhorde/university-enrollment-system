from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('manage/', views.course_list_admin, name='manage_list'),
    path('create/', views.create_course, name='create'),
    path('edit/<int:course_id>/', views.edit_course, name='edit'),
    path('delete/<int:course_id>/', views.delete_course, name='delete'),
]