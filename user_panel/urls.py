from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout_user/',views.logout_user,name='logout'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register,name='register'),
    path('forgot-password',views.forgotPassword,name='forgot-password'),
    path('change-password/<str:id>/',views.changePassword,name='change-password'),
    path('ajax/checkUserName/',views.checkUserName,name='checkUserName'),
    path('ajax/forgetUserField/',views.forgetUserField,name='checkUserName'),
]