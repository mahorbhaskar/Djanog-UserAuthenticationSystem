from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.login_user,name='login'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('forgot-password',views.forgotPassword,name='forgot-password'),
    path('change-password/<str:id>/',views.changePassword,name='change-password'),
    path('ajax/checkUserName/',views.checkUserName,name='checkUserName'),
    path('ajax/checkEmailField/',views.checkEmailField,name='checkEmailField'),


]