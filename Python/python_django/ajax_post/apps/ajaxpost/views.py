from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages 
from .models import *
from django.core import serializers

def index(request):
    return render(request,"ajaxpost/index.html")

def all_html(request):         
    return render(request, "ajaxpost/all.html", {'notes':Note.objects.all()})

def create(request):
    Note.objects.create(text=request.POST['text'])  
    return redirect("/all.html")