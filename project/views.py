from django.shortcuts import render
from django.http import HttpResponse

def aboutme(request):
    return render(request, 'aboutme.html',{})