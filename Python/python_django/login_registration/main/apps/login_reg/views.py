from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt 

# Create your views here.
def index(request):
    print("User is at the index")
    return render(request, "login_reg/index.html", { 'Users' : User.objects.all()})

def create(request):
    print("User is at the create session")
    if 'id' not in request.session:
        request.session['id'] = 99999999
    # if 'log_type' not in request.session:
    #     request.session['log_type'] = "logged in!"
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/")
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
        request.session['id'] = user.id
        request.session['log_type'] = request.POST['log_type']
    print("User created a new user")
    request.session['email'] = request.POST['email']
    return redirect("/success")

def login(request):
    # login = request.POST['log_type']
    request.session['log_type'] = request.POST['log_type']
    request.session['email'] = request.POST['email']
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/")
    return redirect("/success")


def success(request):
    id = request.session['email']
    context = { 
        'id' : User.objects.get(email=id).id,
        'first_name' : User.objects.get(email=id).first_name,
        "login" : request.session['log_type']
    }
    request.session.clear()
    print("User is at the success page")
    return render(request, "login_reg/success.html",context)