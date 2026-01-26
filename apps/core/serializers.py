from rest_framework import serializers
from apps.accounts.models import User
from apps.courses.models import Course
from apps.students.models import Enrollment

class CourseSerializer(serializers.ModelSerializer):
    professor_name = serializers.CharField(source='professor.get_full_name', read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'capacity', 'professor_name', 'day', 'start_time', 'end_time', 'location']

class EnrollmentSerializer(serializers.ModelSerializer):
    course_details = CourseSerializer(source='course', read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'course', 'course_details', 'created_at']