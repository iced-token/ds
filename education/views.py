from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from education.models import Student, Teacher, Course
from education.serializers import StudentSerializer, TeacherSerializer, CreateUserSerializer, UpdateUserSerializer, CourseSerializer
from django.db import transaction

# Create your views here.

class UserMixin(ModelViewSet):

    def create(self, request, *args, **kwargs):
        data = request.data
        user_serializer = CreateUserSerializer(data=data.get('user'))
        serializer = self.get_serializer(data=data.get('data'))
        user_serializer.is_valid(raise_exception=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, user_serializer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        partial = kwargs.pop('partial')
        instance = self.get_object()
        user_serializer = UpdateUserSerializer(data=data.get('user'), instance=instance.user, partial=partial)
        serializer = self.get_serializer(data=data.get('data'), instance=instance, partial=partial)
        user_serializer.is_valid(raise_exception=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer, user_serializer)
        return Response(serializer.data)
    
    @transaction.atomic
    def perform_create(self, serializer, user_serializer):
        user = user_serializer.save()
        serializer.save(user=user)
    
    @transaction.atomic
    def perform_update(self, serializer, user_serializer):
        user = user_serializer.save()
        serializer.save(user=user)

class StudentViewSet(UserMixin, ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class TeacherViewSet(UserMixin, ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]