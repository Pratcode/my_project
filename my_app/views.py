from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html',
                  {'name': 'jubin nautiyal',
                   'pro': 'Network engineer',
                   'exp1': 'Product designer at apple from 2011 to present',
                   'exp2': 'UI designer at theme from 2011 to present',
                   'skl': 'python , django, php'})


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    return render(request, 'contact.html')
