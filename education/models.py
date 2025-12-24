from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Course(models.Model):
    name = models.TextField()

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='students')
    last_payment = models.DateField(null=True, blank=True)
    next_payment = models.DateField(null=True, blank=True)

class Teacher(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers')
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    stars = models.PositiveIntegerField()
    duration = models.DurationField(null=True, blank=True)
    previous_price = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField()
    skills = models.JSONField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and self.stars > 5:
            raise ValueError('stars must be one of (0, 1, 2, 3, 4, 5)')
        super().save(*args, **kwargs)

        



