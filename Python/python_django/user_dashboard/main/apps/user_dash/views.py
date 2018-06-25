from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Review, Comment
import bcrypt 

# Create your views here.
def index(request):
    print("***********cigar guy is at index***********")    
    return render(request, "user_dash/index.html")

def signin(request):
    print("***********cigar guy is at the sign in***********")
    return render(request, "user_dash/signin.html")

def register(request):
    print("***********cigar guy is at the register page***********")
    return render(request, "user_dash/register.html")

# this processes a new user form
def create(request):
    request.session['email'] = request.POST['email']
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        print("we found some errors")
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/register")
    else:
        print("*****cigar guy passed validations*****")
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
        
        id = request.session['email']
        user = User.objects.get(email=id)

        request.session['level'] = user.admin
        request.session['name'] = user.first_name
        request.session['email'] = user.email
        print("***********we have a new cigar guy***********")
        return redirect('/dashboard')    
    
def show(request, id):
    
    # Reviews = []
    # Comments = []
    # for i in this_user.has_reviews.all():
    #     Reviews.append([i.user.first_name, i.user.last_name, i.message, i.user.created_at, i.id])
    
    # for i in Review.objects.filter(user__id=id):
    #     Reviews.append([i.user.first_name, i.user.last_name, i.message, i.user.created_at, i.id])
    # for i in Comment.objects.filter(user__id=id):
    #     Comments.append([i.user.first_name, i.user.last_name, i.message, i.user.created_at, i.id])
    # print(Comments)
    # print(Reviews)
    email = request.session['email']
    poster = User.objects.get(email=email)
    # user = User.objects.get()
    # id = user.id
    # print("***********cigar guy is lookin at",user.first_name, 
    # user.last_name,"profile***********")
    Context = { 
        'user_id' : poster.id,
        # 'first_name' : user.first_name,
        # 'last_name' : user.last_name,
        # 'Review' : Reviews,
        # 'Comment' : Comments,
        'first': User.objects.get(id=id).first_name,
        'last': User.objects.get(id=id).last_name,
        'created_at': User.objects.get(id=id).created_at,
        'desc': User.objects.get(id=id).desc,
        'email': User.objects.get(id=id).email,
        'id': User.objects.get(id=id).id,
        'User' : User.objects.all,
    }
    print(Context)
    return render(request, "user_dash/show.html", Context)

def show_post(request):
    print("Cigar guy is posting a review")
    post = request.POST['review']
    id = request.session['email']
    user = User.objects.get(email=id)
    Review.objects.create(message=post, user=user)
    return redirect("/users/show/"+request.POST['poster'])

def comment(request):
    print("Cigar guy is posting a review")
    post = request.POST['commentbox']
    id = request.session['email']
    user = User.objects.get(email=id)
    Comment.objects.create(message=post, user=user)
    return redirect("/users/show/"+request.POST['poster'])

def dash(request):
    print("***********cigar guy is at the dashboard***********")
    Cigars = { 
        'User' : User.objects.all
    }
    return render(request, "user_dash/dashboard.html", Cigars)

def dash_admin(request):
    print("!!!!!!!!!!cigar admin is at the dashboard!!!!!!!!!!")
    return render(request, "user_dash/admin_dash.html")

def new(request):
    print("***********a brand new cigar guy has arrived***********")
    return render(request, "user_dash/new.html")

def edit(request):
    print("***********cigar guy is editing his profile***********")
    return render(request, "user_dash/edit.html")

def edit_admin(request, id):
    print("!!!!!!!!!!cigar admin is looking to edit a cigar guy!!!!!!!!!!")
    return render(request, "user_dash/admin_edit.html")

def logoff(request):
    print("***********cigar guy has logged off***********")
    # request.session.clear()
    return redirect("/")

def update(request):
    print("***********cigar guy is trying to update their info***********")
    return redirect("/")







    # this_user = User.objects.get(id=id)
    # id = this_user.id
    # # print("***********cigar guy is lookin at",user.first_name, 
    # # user.last_name,"profile***********")
    # Reviews = []
    # Comments = []
    # for i in this_user.has_reviews.all():
    #     Reviews.append([i.user.first_name, i.user.last_name, i.message, i.user.created_at, i.id])
    
    # # for i in Review.objects.filter(user__id=id):
    # #     Reviews.append([i.user.first_name, i.user.last_name, i.message, i.user.created_at, i.id])
    # for i in Comment.objects.filter(user__id=id):
    #     Comments.append([i.user.first_name, i.user.last_name, i.message, i.user.created_at, i.id])
    # print(Comments)
    # print(Reviews)
    # email = request.session['email']
    # poster = User.objects.get(email=email)
    # # user = User.objects.get()
    # # id = user.id
    # print("***********cigar guy is lookin at",user.first_name, 
    # user.last_name,"profile***********")






# def post(request):
#     print(request.POST['log_type'])
#     print("User is posting a review")
#     post = request.POST['review']
#     id = request.session['email']
#     user = User.objects.get(email=id)
#     Review.objects.create(message=post, user=user)

#     return redirect("/wall")

# def newuser(request):
#     print("User has submitted a new user form")
#     if 'id' not in request.session:
#         request.session['id'] = 99999999
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for key,val in errors.items():
#             messages.error(request,val)
#         return redirect("/create")
#     else:
#         hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
#         user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
#         request.session['id'] = user.id
#         request.session['log_type'] = request.POST['log_type']
#     print("User created a new user")
#     request.session['email'] = request.POST['email']
#     return redirect("/wall")

# def create(request):
#     print("User is creating a new profile")

#     return render(request,"the_wall/create.html")

# def process(request):
#     print("user is logging in")
#     # request.session['log_type'] = request.POST['log_type']
#     request.session['email'] = request.POST['email']
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for key,val in errors.items():
#             messages.error(request,val)
#         return redirect("/")
#     id = request.session['email']
#     print(id,"this is the users email")
#     user = User.objects.get(email=id).first_name
#     request.session['name'] = user
#     return redirect("/wall")

# def wall(request):
#     id = request.session['email']
#     user = User.objects.get(email=id)
#     request.session['id'] = user.id
#     context = { 
#         'id' : user.id,
#         'first_name' : user.first_name,
#         'last_name' : user.last_name,
#         'review' : Review.objects.all(),
#         'comment' : Comment.objects.all()
#     }
#     # request.session.clear()
#     print("User is at the wall")
#     return render(request, "the_wall/wall.html", context)

# def logout(request):
#     request.session.clear()
#     print("User is logging out")
#     return redirect("/")

# # def delete(request):
# #     id = request.POST['delete']
# #     print(id)
# #     review = Review.objects.get(id=id)
# #     if review.user.id == request.session['id']:
# #         review.delete()
# #         review.save()
# #     else:
# #         messages.warning(request, "You can only delete your own reviews!")
# #     print("User is deleting a review")
# #     return redirect("/wall")

# def comment(request):
#     comment = request.POST['commentbox']
#     print(comment, "****************************************************************************************")
#     id = request.session['id']
#     print(request.POST['review_id'])
#     print(comment, "****************************************************************************************")
#     user = User.objects.get(id=id)
#     review_id = str(request.POST['review_id'])
#     print(review_id)
#     review = Review.objects.get(id=review_id)
#     Comment.objects.create(message=comment, user=user, review=review)

#     return redirect("/wall")


    
# def create(request):
#     print("User is at the create session")
#     if 'id' not in request.session:
#         request.session['id'] = 99999999
#     # if 'log_type' not in request.session:
#     #     request.session['log_type'] = "logged in!"
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for key,val in errors.items():
#             messages.error(request,val)
#         return redirect("/")
#     else:
#         hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
#         user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
#         request.session['id'] = user.id
#         request.session['log_type'] = request.POST['log_type']
#     print("User created a new user")
#     request.session['email'] = request.POST['email']
#     return redirect("/success")


#     def login(request):
#     # login = request.POST['log_type']
#     request.session['log_type'] = request.POST['log_type']
#     request.session['email'] = request.POST['email']
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for key,val in errors.items():
#             messages.error(request,val)
#         return redirect("/")
#     return redirect("/success")


# def success(request):
#     id = request.session['email']
#     context = { 
#         'id' : User.objects.get(email=id).id,
#         'first_name' : User.objects.get(email=id).first_name,
#         "login" : request.session['log_type']
#     }
#     request.session.clear()
#     print("User is at the success page")
#     return render(request, "login_reg/success.html",context)