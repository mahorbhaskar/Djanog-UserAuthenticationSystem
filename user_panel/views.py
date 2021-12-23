from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Question, UserQuestionModel, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'user_panel/home.html')


# Function to Register the User
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        question = request.POST.get('question',None)
        answer = request.POST.get('answer',None)
        user = User(username=username, password = password)
        user.is_staff = False
        user.set_password(password)
        user.save()
        token = str(uuid.uuid4())
        profile = Profile.objects.create(user=user,forget_password_token=token)
        profile.save()
        question_table = Question.objects.get(question=question)
        user_data2 = UserQuestionModel.objects.create(question=question_table, user=user, answer=answer)
        user_data2.save()

        messages.info(request,username+' Your have Registered Successfully.')
        return redirect('login')
    else:    
        return render(request, 'user_panel/register.html')


# Function to LogIn the User
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password =password)
        print(user)
        if user is not None:
            login(request,user)    
            return redirect('home')
        else:
            messages.warning(request,'wrong credentials')
            return redirect('login')
    return render(request,'user_panel/login.html')

# changePassword function to change password
def changePassword(request,id):
    if request.method == 'POST':
        password = request.POST.get('password')
        profile = Profile.objects.get(forget_password_token=id).user
        user = User.objects.get(username = profile)
        user.set_password(password)
        user.save()
        print(user.username)
        print('change password',password)
        messages.success(request,'Password Changed Successfully! Please LogIn.')
        return redirect('login')
    return render(request,'user_panel/change-password.html')

# Forgot Password Page if forget your password
def forgotPassword(request):
    username = request.POST.get('username',None)
    question = request.POST.get('question',None)
    answer = request.POST.get('answer',None)
    if User.objects.filter(username=username).exists():
        question_id = Question.objects.get(question=question)
        user_id = User.objects.get(username=username)
        if UserQuestionModel.objects.filter(question=question_id,answer=answer,user=user_id).exists:
            profile = Profile.objects.get(user=user_id)
            user_email = user_id.username
            print(user_email)
            ftoken = profile.forget_password_token
            print(ftoken)
            mail_message = f'Hi, click on the link to reset your password http://127.0.0.1:8000/change-password/{ftoken}/'
            send_mail('Password Reset Request',mail_message,settings.EMAIL_HOST_USER,[user_email],fail_silently = False)
            messages.success(request,'MAIL SENT')
            return redirect('forgot-password')
    return render(request,'user_panel/forgot-password.html')


#validations part
def checkUserName(request):
    username = request.GET.get('username',None)
    data = {
        'is_taken': User.objects.filter(username=username).exists(),
    }
    if data['is_taken']:
        data['error_message'] = 'usrname already exists'
    return JsonResponse(data)
#email Validation
def checkEmailField(request):
    email = request.GET.get('email',None)
    data = {
        'is_taken': User.objects.filter(email=email).exists(),
    }
    if data['is_taken']:
        data['error_message'] = 'eamil already exists'
    return JsonResponse(data)