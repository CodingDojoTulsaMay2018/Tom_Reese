from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    print("User is at the index")
    return render(request, "semi_users/index.html", { 'Users' : User.objects.all()})

def new(request):
    print("User is at new")
    return render(request, "semi_users/new.html")

def edit(request, id):
    print("User is at the edit")
    context = { 
        'id' : id,
        'first_name' : User.objects.get(id=id).first_name,
        'last_name' : User.objects.get(id=id).last_name,
        'email' : User.objects.get(id=id).email,
    }

    return render(request, "semi_users/edit.html", context)

def show(request, id):
    context = { 
        'id' : id,
        'first_name' : User.objects.get(id=id).first_name,
        'last_name' : User.objects.get(id=id).last_name,
        'email' : User.objects.get(id=id).email,
        'created_at' : User.objects.get(id=id).created_at,
    }
    print("User is at the show")
    return render(request, "semi_users/show.html", context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/new")
    else:
        print("User is at create")
        print(request.POST['first_name'])
        user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/"+str(user.id))

def destroy(request, id):
    print("User is at destroy")
    User.objects.get(id=id).delete()
    return redirect("/")

def update(request):
    print("User is at the update")
    id = request.POST['id']
    user = User.objects.get(id=id)
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/"+str(user.id)+"/edit")
    else:
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
    return redirect("/"+str(user.id))