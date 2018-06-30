from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages 
from .models import *
from django.core import serializers

def index(request):
    print("User is at the home page")
    return render(request, "ajax_pag/index.html")

def all(request):         
    return render(request, "ajax_pag/all.html", {'Users':User.objects.all()})

def find(request):
    # print(request.POST['from_date'])
    return render(request, "ajax_pag/all.html", {'Users':User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])})
