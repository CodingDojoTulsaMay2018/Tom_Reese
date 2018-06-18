from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Courses
# from .models import User

def index(request):
    print("User is at the index")
    return render(request, "courses/index.html", { 'Courses' : Courses.objects.all()})

def show(request, id):
    context = { 
        'id' : id,
        'name' : Courses.objects.get(id=id).name,
        'desc' : Courses.objects.get(id=id).desc,
        'created_at' : Courses.objects.get(id=id).created_at,
    }
    print("User is at the show")
    return render(request, "courses/show.html", context)

def create(request):
    errors = Courses.objects.basic_validator(request.POST)
    if len(errors):
        print("User had errors in while adding a course")
        for key,val in errors.items():
            messages.error(request,val)
    else:
        print("User is creatng the following course...",request.POST['name'])
        Courses.objects.create(name=request.POST['name'],desc=request.POST['desc'])
    return redirect("/")

def destroy(request, id):
    print("User is at destroy")
    Courses.objects.get(id=id).delete()
    return redirect("/")
