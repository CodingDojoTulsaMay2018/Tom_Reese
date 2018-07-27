from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from django.core import serializers
from .models import User, Player, Messaging
import bcrypt 

def index(request):
    print("User is at the home page")
    return render(request, "auction/index.html")

def login(request):
    print("User is trying to login")
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(username=request.POST['username'])
        request.session['username'] = user.username
        request.session['name'] = user.name
        messages.error(request, "Successfully logged in")
    return redirect('/profile')

def profile(request):
    print("User is at their profile page")
    if 'username' not in request.session:
        messages.error(request, "Must be logged in to view players!")
        return redirect('/') 
    user = User.objects.get(username=request.session['username'])
    spent = 0
    for i in user.has_player.all():
        spent+=i.salary
    space = (150 - spent)
    spots = 16
    count = 0
    for i in user.has_player.all():
        count+=1
    spots -= count

    return render(request, "auction/profile.html",{'Team_Name' : user.team_name,'Slogan' : user.slogan,'Username' : user.username,'Email' : user.email,'ID' : user.id,'Managers' : User.objects.all(),'Cap' : space,'Open' : spots,})




def update(request):
    if 'username' not in request.session:
        messages.error(request, "Must be logged in to view players!")
        return redirect('/') 
    username = request.session['username']
    print(request.POST['username'])
    errors = User.objects.update_validator(request.POST, username)
    if len(errors):
        id = request.POST['id']
        for key, value in errors.items():
            messages.error(request, value)
            return redirect("/profile")
    else:
        user = User.objects.get(username=request.session['username'])
        user.username = request.POST['username']
        user.slogan = request.POST['slogan']
        user.email = request.POST['email']
        user.team_name = request.POST['team_name']
        user.save()
        request.session['username'] = user.username

        messages.error(request, user.name+" has successfully changed their information")    
    id = request.POST['id']
    return redirect("/profile")

def find_player(request):
    return render(request, "auction/players.html", {'Players':Player.objects.filter(name__contains=request.POST['name_includes']).order_by('name')})

def manager_stats(request):
    if 'username' not in request.session:
        messages.error(request, "Must be logged in to view players!")
        return redirect('/')
    print("looking for manager")
    print("got past manager validation check")
    print(request.POST['manager_id'],"*****is the manager id")
    manager=User.objects.get(id=request.POST['manager_id'])
    roster=manager.has_player.all()
    return render(request, "auction/managers.html", {'Managers': User.objects.filter(id=request.POST['manager_id']), 'Roster' : roster})


def roster(request):
    if 'username' not in request.session:
        messages.error(request, "Must be logged in to view players!")
        return redirect('/')
    # , {'Roster': Player.objects.all()}
    return render(request, "auction/roster.html")

# def auction(request):
#     if 'username' not in request.session:
#         messages.error(request, "Must be logged in to view players!")
#         return redirect('/')
#     user = User.objects.get(username=request.session['username'])
#     spent = 0
#     for i in user.has_player.all():
#         spent+=i.salary
#     space = (150 - spent)
#     spots = 16
#     count = 0
#     for i in user.has_player.all():
#         count+=1
#     spots -= count
#     return render(request,"auction/auction.html", {'Cap' : space,'Open' : spots,})

def message_text(request):
    username = request.session['username']
    errors = Messaging.objects.message_validator(request.POST, username)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/auction')
    else:
        user = User.objects.get(username=request.session['username'])
        newpost = Messaging.objects.create(text=request.POST['message_text'], user_id=user.id)
        newpost.save()
        print(newpost,"*******************")
    return render(request, "auction/messages.html", {'Messages': Messaging.objects.all()})


# def create(request):
#     User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], age=request.POST['age'],email_address=request.POST['email'])
#     return render(request, "user_login/all.html", {'users':User.objects.order_by('-id')})

       



# def user_quotes(request, id):
#     if 'user_id' not in request.session:
#         messages.error(request, "Must be logged in to view this page!")
#         return redirect('/')
#     edit = User.objects.get(id=request.session['user_id'])
#     user = User.objects.get(id=id)
#     context = {
#         "Quotes": user.uploaded_quote.all(),
#         'User': user,
#         'Edit' : edit.id
#     }
#     return render(request, "dash/user_quotes.html", context)        

# def quotes(request):
#     if 'user_id' not in request.session:
#         messages.error(request, "Must be logged in to view quotes!")
#         return redirect('/')
#     id = request.session['user_id']
#     user = User.objects.get(id=id)

#     context = {
#         'Quotes': Quote.objects.annotate(count_likes=Count('liked_users')).order_by('-count_likes'),
#         'User' : user
#     }
#     return render(request,'dash/quotes.html',context)

# def create(request):
#     user_id = request.POST['user_id']
#     print("User submitted a quote for validation")
#     errors = Quote.objects.process_quote(request.POST, user_id)
#     print("Out of validations, checking for errors")
#     for key, value in errors.items():
#         messages.error(request, value)
#         return redirect("/quotes")


# def update(request):
#     if 'user_id' not in request.session:
#         messages.error(request, "Must be logged in to view quotes!")
#         return redirect('/') 
#     id = request.session['user_id']
#     print(id)
#     errors = User.objects.update_validator(request.POST, id)
#     if len(errors):
#         id = request.POST['id']
#         for key, value in errors.items():
#             messages.error(request, value)
#             return redirect("/edit/"+id)
#     else:
#         user = User.objects.get(id=request.POST['id'])
#         user.first_name = request.POST['first_name']
#         user.last_name = request.POST['last_name']
#         user.email = request.POST['email']
#         user.save()
#         request.session['user_id'] = user.id
#         request.session['first_name'] = user.first_name
#         request.session['last_name'] = user.last_name
#         messages.error(request, "Successfully changed their information")    
#     id = request.POST['id']
#     return redirect("/edit/"+id)

def logoff(request):
    print("User is logging off")
    # request.session.clear()
    return redirect("/")

# def delete(request):
#     print("User is deleting a secret")
#     this_quote = Quote.objects.get(id=request.POST['quote_id'])
#     this_quote.delete()
#     return redirect('/quotes')

# def like(request):
#     id = request.session['user_id']
#     liked_users = Quote.objects.process_like(request.POST, id)
#     return redirect('/quotes')



#AJAX VIEWS

# def all_json(request):
#     users = User.objects.all()
#     return HttpResponse(serializers.serialize("json", users), content_type='application/json')

# def all_html(request): 
#     return render(request, "user_login/all.html", {'users':User.objects.all()})

# def find(request):
#     if not request.POST['first_name_starts_with']:
#         return HttpResponse('awaiting input...')
#     return render(request, "user_login/all.html", {'users':User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])})

# def create(request):
#     User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], age=request.POST['age'],email_address=request.POST['email'])
#     return render(request, "user_login/all.html", {'users':User.objects.order_by('-id')})