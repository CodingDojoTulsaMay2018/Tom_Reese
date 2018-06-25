from django.shortcuts import render, HttpResponse, redirect
from .models import User, Wish, UserManager
from django.contrib import messages
from django.db.models import Count
import bcrypt


def index(request):
    return render(request, 'wish/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name = request.POST['name'], username = request.POST['username'], password = hashed)
        request.session['user_id'] = user.id
        request.session['name'] = user.name
        messages.error(request, "Successfully registered!")
        return redirect('/dashboard')


def login(request):
    if User.objects.filter(username = request.POST['username']):
        user = User.objects.get(username = request.POST['username'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['name'] = user.name
            messages.error(request, "Successfully logged in!")
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect ('/')
    else:
        messages.error(request, "Invalid username or password")
        return redirect('/')



def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view this page!")
        return redirect('/')
    id = request.session['user_id']
    this_user = User.objects.get(id=id)
    actions = []
    for i in this_user.has_wish.all():
        if this_user.id == i.id:
            continue
        if this_user.id == i.dreamer.id:
            action = "Delete"
            actions.append([action, i.id,i.wish, i.dreamer.name, i.created_at])
        else:
            action = "Remove"
            actions.append([action, i.id,i.wish, i.dreamer.name, i.created_at])

    others = []
    for i in Wish.objects.exclude(dreamer__id=this_user.id):
        action = "Add"
        others.append([action, i.id,i.wish, i.dreamer.name, i.created_at])


    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'first_name': request.session['name'],
        "Wishes": actions,
        'Others': others
    }
  
    return render(request, 'wish/dashboard.html', context)

def add(request):
    add = request.POST['add']
    id = request.session['user_id']
    user = User.objects.get(id=id)
    this_wish = Wish.objects.get(id=request.POST['wishid'])
    this_wish.has_dreamers.add(user)
    user.has_wish.add(this_wish)
    return redirect('/dashboard')

def remove(request):
    if request.POST['methods'] == "Delete":
        wishid = request.POST['wishid']
        id = request.session['user_id']
        user = User.objects.get(id=id)
        Wish.objects.get(id=wishid).delete()
    if request.POST['methods'] == "Remove":
        wishid = request.POST['wishid']
        this_wish=Wish.objects.get(id=wishid)
        id = request.session['user_id']
        this_user = User.objects.get(id=id)
        this_user.has_wishes.remove(this_wish)
        
    return redirect('/dashboard')

def create(request):
    # errors = User.objects.validator(request.POST)

    # add = request.POST['add']
    id = request.session['user_id']
    user = User.objects.get(id=id)
    # Wish.objects.create(wish = add, dreamer=user)
    return render(request, 'wish/wish_create.html')


def addwish(request):
    errors = Wish.objects.process_wish(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wish_items/create')
    else:
        id = request.session['user_id']
        this_user = User.objects.get(id=id)
        this_wish = Wish.objects.create(wish=request.POST['wish'])
        this_user.has_wishes.add(this_wish)
        print("wish created successfully")
    return redirect("/dashboard")

def items(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view this page!")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    this_wish = Wish.objects.get(id=id)
    
    items = []
    for i in this_wish.has_dreamers.all():
        if user.id == i.id:
            continue
        else:
            items.append([i.name])
    context = {
        'item': Wish.objects.get(id=id),
        "Wishes": items,
    }
    return render(request, "wish/wish_items.html", context)



def logoff(request):
    request.session.clear()
    return redirect('/')

