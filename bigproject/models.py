from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image')

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orientation_lesson_1_practice = models.BooleanField(default=False)
    orientation_lesson_1_quiz = models.BooleanField(default=False)
    orientation_lesson_2 = models.BooleanField(default=False)
    orientation_lesson_2_quiz = models.BooleanField(default=False)
    orientation_lesson_3 = models.BooleanField(default=False)
    orientation_lesson_3_practice = models.BooleanField(default=False)
    orientation_lesson_3_quiz = models.BooleanField(default=False)
    analyzing_behavior_lesson_1 = models.BooleanField(default=False)
    analyzing_behavior_lesson_1_practice = models.BooleanField(default=False)
    analyzing_behavior_lesson_1_quiz = models.BooleanField(default=False)
    analyzing_behavior_lesson_2 = models.BooleanField(default=False)
    analyzing_behavior_lesson_2_practice = models.BooleanField(default=False)
    analyzing_behavior_lesson_2_quiz = models.BooleanField(default=False)
    intro_mindfulness_lesson_1 = models.BooleanField(default=False)