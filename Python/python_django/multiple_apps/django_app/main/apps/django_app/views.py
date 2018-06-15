from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later dispay all the list of blogs"
    print('at the index')
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    print('new function invoked')
    return HttpResponse(response)

def create(request):
    print('create function invoked')
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

