from django.shortcuts import render
from django.http import *
from .models import CallBackMail, CallBackPhone
from django.core.mail import BadHeaderError, send_mail

# Create your views here.

home_url = 'http://127.0.0.1:3000'


def index(request):
    return render(request, 'index.html', {'home_url': home_url})


def about(request):
    return render(request, 'about.html', {'home_url': home_url})


def contact(request):
    return render(request, 'contact.html', {'home_url': home_url})


def sandmail(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        sender = CallBackMail()
        sender.name = name
        sender.email = email
        sender.subject = subject
        sender.message = message
        sender.save()
        from_email = 'adminsmv'
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email,
                          ['mukhinsergey@list.ru'])
            except BadHeaderError:
                return render(request, 'invalidto.html', {'home_url': home_url})
            return render(request, 'mailto.html', {"name": name})
        else:
            return render(request, 'contact.html', {'home_url': home_url})
    else:
        return render(request, 'contact.html', {'home_url': home_url})


def popupmail(request):
    if request.method == "POST":
        sender = CallBackPhone()
        sender.name = request.POST.get("name")
        sender.phone = request.POST.get("phone")
        sender.save()
        return render(request, 'mailto.html', {"name": sender.name})
    else:
        return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')
