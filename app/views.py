from django.shortcuts import render
from app.models import *

# Create your views here.

def home(request):
    d={
        'name':'Diksha',
        'age':25,
        'pay':3200
    }
    return render(request,'home.html',d)

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pass')
        email=request.POST.get('email')
        cdo=Details(username=un,
                    password=pw,
                    email=email)
        cdo.save()
        return render(request,'login.html')

    return render(request,'register.html')
