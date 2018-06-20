from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Review, Comment
import bcrypt 

# Create your views here.
def index(request):
    print("User is at the index")
    return render(request, "the_wall/index.html")

def post(request):
    print(request.POST['log_type'])
    print("User is posting a review")
    post = request.POST['review']
    id = request.session['email']
    user = User.objects.get(email=id)
    Review.objects.create(message=post, user=user)

    return redirect("/wall")

def newuser(request):
    print("User has submitted a new user form")
    if 'id' not in request.session:
        request.session['id'] = 99999999
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/create")
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
        request.session['id'] = user.id
        request.session['log_type'] = request.POST['log_type']
    print("User created a new user")
    request.session['email'] = request.POST['email']
    return redirect("/wall")

def create(request):
    print("User is creating a new profile")

    return render(request,"the_wall/create.html")

def process(request):
    print("user is logging in")
    # request.session['log_type'] = request.POST['log_type']
    request.session['email'] = request.POST['email']
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/")
    id = request.session['email']
    print(id,"this is the users email")
    user = User.objects.get(email=id).first_name
    request.session['name'] = user
    return redirect("/wall")

def wall(request):
    id = request.session['email']
    user = User.objects.get(email=id)
    request.session['id'] = user.id
    context = { 
        'id' : user.id,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'review' : Review.objects.all(),
        'comment' : Comment.objects.all()
    }
    # request.session.clear()
    print("User is at the wall")
    return render(request, "the_wall/wall.html", context)

def logout(request):
    request.session.clear()
    print("User is logging out")
    return redirect("/")

# def delete(request):
#     id = request.POST['delete']
#     print(id)
#     review = Review.objects.get(id=id)
#     if review.user.id == request.session['id']:
#         review.delete()
#         review.save()
#     else:
#         messages.warning(request, "You can only delete your own reviews!")
#     print("User is deleting a review")
#     return redirect("/wall")

def comment(request):
    comment = request.POST['commentbox']
    print(comment, "****************************************************************************************")
    id = request.session['id']
    print(request.POST['review_id'])
    print(comment, "****************************************************************************************")
    user = User.objects.get(id=id)
    review_id = str(request.POST['review_id'])
    print(review_id)
    review = Review.objects.get(id=review_id)
    Comment.objects.create(message=comment, user=user, review=review)

    return redirect("/wall")