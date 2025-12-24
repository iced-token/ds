from rest_framework.routers import DefaultRouter
from django.urls import path, include
from education.views import *

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls))
]