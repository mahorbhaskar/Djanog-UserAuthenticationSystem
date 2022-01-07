from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=60,null=True)

    def __str__(self):
        return self.question

class UserQuestionModel(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

