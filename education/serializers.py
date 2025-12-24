from rest_framework.serializers import ModelSerializer
from education.models import Student, Teacher, Course
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'password', 'username', 'email']
        read_only_fields = ['id']

class UpdateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class StudentSerializer(ModelSerializer):

    user = UpdateUserSerializer()

    class Meta:
        model = Student
        exclude = []
        extra_kwargs = {
            'courses': { 'allow_empty': True },
            'user': { 'required': False }
        }

class TeacherSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        exclude = []

class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        exclude = []
