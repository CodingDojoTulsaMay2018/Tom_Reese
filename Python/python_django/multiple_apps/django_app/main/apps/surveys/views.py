from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = "placeholder to display all the surveys created"
    print('at the index')
    return HttpResponse( context)

def new(request):
    response = "placeholder to display a new form to create a new survey"
    print('new function invoked')
    return HttpResponse(response)
