from django.contrib import admin
from .models import Question, UserQuestionModel, Profile
# Register your models here.
admin.site.register(Question)
admin.site.register(UserQuestionModel)
admin.site.register(Profile)