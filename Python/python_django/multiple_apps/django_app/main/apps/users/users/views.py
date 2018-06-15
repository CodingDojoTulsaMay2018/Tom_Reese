from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to dispay all the surveys created"
    print('at the index')
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey"
    print('new function invoked')
    return HttpResponse(response)