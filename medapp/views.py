from django.shortcuts import render, redirect
from .models import Media, Contact
from django.contrib import messages


# Create your views here.


def resume(request):
    media_suff = Media.objects.all()
    return render(request, 'resume.html', {'media_stuff': media_suff})


def contact(request):
    media_suff = Media.objects.all()
    return render(request, 'contact.html', {'media_stuff': media_suff})


def msg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        msg_save = Contact(contact_name=name, contact_email=email, contact_body=message)
        msg_save.save()
        messages.info(request, 'Message has been sent')
        return redirect('contact')
