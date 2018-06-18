from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Cigars
from decimal import Decimal
# from .models import User

def index(request):
    print("User is looking for cigars")
    
    return render(request, "amadon/index.html", { 'Cigars' : Cigars.objects.all()})


def checkout(request):
    print("User is at the checkout")
    id = int(request.session['id'])
    context = { 
        'id' : id,
        'name' : Cigars.objects.get(id=id).name,
        'total' : request.session['total'],
        'number' : request.session['number'],
        'final' : request.session['sumtotal']
    }
    return render(request,"amadon/checkout.html", context)

def process(request):
    print("User purchased",request.POST['quantity'],"of the following cigars...",request.POST['id'])
    
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'number' not in request.session:
        request.session['number'] = 0
    if 'sumtotal' not in request.session:
        request.session['sumtotal'] = 0
    if 'quantity' not in request.session:
        request.session['quantity'] = 0
    request.session['id'] = request.POST['id']
    id = int(request.session['id'])
    item = Cigars.objects.get(id=id)
    price = float(item.price)
    quantity = float(request.POST['quantity'])
    request.session['quantity'] = int(request.POST['quantity'])
    request.session['number'] += request.session['quantity']
    request.session['total'] = float(price * quantity)
    print(request.session['total'])
    print(type(request.session['total']))
    print(type(request.session['sumtotal']))
    finalval=request.session['sumtotal'] + request.session['total']
    request.session['sumtotal'] = finalval

    return redirect("/checkout")

def clear(request):
    print("User has cleared their session")
    request.session.clear()
    return redirect("/")