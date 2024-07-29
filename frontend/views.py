from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def f_index(request):
    return render(request, 'home.html')

def contact_mail(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        mailto = request.POST.get('to')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            subject, 
            F'FROM: <{mailto}> \nTO: <{settings.EMAIL_HOST_USER}>\nSUBJECT: {subject} \n\nMESSAGE: {message}', 
            settings.EMAIL_HOST_USER, 
            [mailto]
        )
        messages.success(request, 'Mail Send Successfully')
        return redirect(f_index)
