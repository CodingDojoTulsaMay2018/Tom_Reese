from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from .models import User, Secret
import bcrypt 

def index(request):
    print("User is at the home page")
    return render(request, "tulsa_secrets/index.html")

def register(request):
    print("User is submitting a new registration form")
    if not request.POST['first_name'] or not request.POST['last_name']:
        messages.error(request, "Cannot submit blank data!")
        return redirect('/')
    else:
        errors = User.objects.create_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            print("User did not register successfully")
            return redirect('/')
        else:
            hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            print(user.first_name, user.last_name,"has successfully registered")
            return redirect('/profile')        

def login(request):
    print("User is trying to login")
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        messages.error(request, "Successfully logged in")
        return redirect('/profile')
            

def profile(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view profile!")
        return redirect('/')
    id = request.session['user_id']
    user = User.objects.get(id=id)
    print(user.first_name, user.last_name, "is at the profile page")

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'first_name': request.session['first_name'],
        "Secrets": Secret.objects.annotate(count_likes=Count('liked_users')).order_by('-created_at'),
    }
    return render(request,'tulsa_secrets/profile.html',context)

def secret(request):
    user_id = request.session['user_id']
    print("User submitted a secret for validation")
    errors = Secret.objects.process_secret(request.POST, user_id)
    print("Out of validations, checking for errors")
    for key, value in errors.items():
        messages.error(request, value)
        return redirect("/profile")
    
def secrets(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view secrets!")
        return redirect('/') 

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'first_name': request.session['first_name'],
        "Secrets": Secret.objects.annotate(count_likes=Count('liked_users')).order_by('-count_likes')[:5],
    }

    return render(request,'tulsa_secrets/secrets.html', context)

def logoff(request):
    print("User is logging off")
    request.session.clear()
    return redirect("/")

def delete(request):
    print("User is deleting a secret")
    this_secret = Secret.objects.get(id=request.POST['secret_id'])
    this_secret.delete()
    if request.POST['page'] == 'profile':
        return redirect('/profile')
    if request.POST['page'] == 'secrets':
        return redirect('/secrets')

def like(request):
    liked_users = Secret.objects.process_like(request.POST)
    if request.POST['page'] == 'profile':
        return redirect('/profile')
    if request.POST['page'] == 'secrets':
        return redirect('/secrets')
    return redirect('/profile')
     