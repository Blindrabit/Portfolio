from django.shortcuts import render
from django.http import HttpResponse

def aboutme(request):
    return render(request, 'aboutme.html',{})

def index(request):
    return render(request, 'index.html',{})

def datascience(request):
    return render(request, 'datascience.html',{})

def django(request):
    return render(request, 'django.html',{})