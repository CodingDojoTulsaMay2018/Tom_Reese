from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages 
from .models import *
from django.core import serializers
# Create your views here.


def index(request):
    return render(request,"user_login/index.html")

def all_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type='application/json')

def all_html(request): 
    return render(request, "user_login/all.html", {'users':User.objects.all()})

def find(request):
    if not request.POST['first_name_starts_with']:
        return HttpResponse('awaiting input...')
    return render(request, "user_login/all.html", {'users':User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])})

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], age=request.POST['age'],email_address=request.POST['email'])
    return render(request, "user_login/all.html", {'users':User.objects.order_by('-id')})