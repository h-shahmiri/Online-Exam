from django.db import models
from django.contrib.auth.models import User
from exam.models import Questions

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_question = models.ManyToManyField(Questions)
    score = models.IntegerField()

