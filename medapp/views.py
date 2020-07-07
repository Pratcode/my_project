from django.shortcuts import render
from .models import Media
# Create your views here.


def resume(request):
    media_suff = Media.objects.all()
    return render(request, 'resume.html', {'media_stuff': media_suff})


def contact(request):
    media_suff = Media.objects.all()
    return render(request, 'contact.html', {'media_stuff': media_suff})