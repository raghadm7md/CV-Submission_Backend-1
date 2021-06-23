from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

# ********* not tset it yet **********

def signup(request):
    if request.method == 'POST':
        # firstname=request.POST['FirstName']
        # lastname=request.POST['LastNmae']
        email=request.POST['Email']
        username=request.POST['username']
        password=request.POST['password']

        NewUser= User.objects.create_user(
            username=username,
            password=password
        )
        login(request,NewUser)
        subject = 'welcome to our website'
        message = f'Hi {NewUser.username}, thank you for registering in CV-profile cubmission.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
    return render (request)

