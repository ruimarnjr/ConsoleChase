from django.shortcuts import render
from .models import ContactUs
from django.contrib import messages

# Create your views here.

def index(request):
    """ A view to return the index page and display the contact form"""
    if request.method == 'POST':
        contact=ContactUs()
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.full_name = full_name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, 'home/index.html')
