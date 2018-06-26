from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from .models import User, Quote
import bcrypt 

def index(request):
    print("User is at the home page")
    return render(request, "dash/index.html")

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
            request.session['last_name'] = user.last_name
            print(user.first_name, user.last_name,"has successfully registered")
            return redirect('/quotes')        

def login(request):
    print("User is trying to login")
    if not request.POST['email'] or not request.POST['password']:
        messages.error(request, "Cannot submit blank data!")
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        messages.error(request, "Successfully logged in")
        return redirect('/quotes')

def user_quotes(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view this page!")
        return redirect('/')
    edit = User.objects.get(id=request.session['user_id'])
    user = User.objects.get(id=id)
    context = {
        "Quotes": user.uploaded_quote.all(),
        'User': user,
        'Edit' : edit.id
    }
    return render(request, "dash/user_quotes.html", context)        

def quotes(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view quotes!")
        return redirect('/')
    id = request.session['user_id']
    user = User.objects.get(id=id)

    context = {
        'Quotes': Quote.objects.annotate(count_likes=Count('liked_users')).order_by('-count_likes'),
        'User' : user
    }
    return render(request,'dash/quotes.html',context)

def create(request):
    user_id = request.POST['user_id']
    print("User submitted a quote for validation")
    errors = Quote.objects.process_quote(request.POST, user_id)
    print("Out of validations, checking for errors")
    for key, value in errors.items():
        messages.error(request, value)
        return redirect("/quotes")

def edit(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view quotes!")
        return redirect('/') 
    user = User.objects.get(id=request.session['user_id'])

    context = {
        'First' : user.first_name,
        'Last' : user.last_name,
        'Email' : user.email,
        'ID' : user.id
    }
    return render(request, "dash/edit.html", context)

def update(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view quotes!")
        return redirect('/') 
    
    errors = User.objects.update_validator(request.POST)
    if len(errors):
        id = request.POST['id']
        for key, value in errors.items():
            messages.error(request, value)
            return redirect("/edit/"+id)
    else:
        user = User.objects.get(id=request.POST['id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        messages.error(request, "Successfully changed their information")    
    id = request.POST['id']
    return redirect("/edit/"+id)

def logoff(request):
    print("User is logging off")
    request.session.clear()
    return redirect("/")

def delete(request):
    print("User is deleting a secret")
    this_quote = Quote.objects.get(id=request.POST['quote_id'])
    this_quote.delete()
    return redirect('/quotes')

def like(request):
    id = request.session['user_id']
    liked_users = Quote.objects.process_like(request.POST, id)
    return redirect('/quotes')
     
