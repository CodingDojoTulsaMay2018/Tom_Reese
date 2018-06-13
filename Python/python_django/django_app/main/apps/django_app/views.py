from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    print('at the index')
    return render(request, "django_app/index.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    print('new function invoked')
    return HttpResponse(response)

def create(request):
    print('create function invoked')
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

def show(request, number):
    print('show function invoked')
    return HttpResponse("placeholder to display blog " +number)

def edit(request, number):
    print('edit function invoked')
    return HttpResponse("placeholder to edit blog  " +number)

def destroy(request, number):
    print('delete function invoked')
    return redirect('/')

def back(request):
    print('delete function invoked')
    return redirect('/')