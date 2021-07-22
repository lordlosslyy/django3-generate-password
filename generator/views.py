from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def home(request): 
    return render(request, 'generator/home.html', {'password': 'sfsdf'})

def password(request): 
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))    
    
    # 12 there is default value
    length = int(request.GET.get('length', 12))
		
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):  
    return render(request, 'generator/about.html')