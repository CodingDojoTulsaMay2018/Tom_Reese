from django.shortcuts import render
from .models import Dojos, Ninjas
# Create your views here.
def index(request):
    context = {"Ninjas": Dojos.objects.all()}
    print(context['Ninjas'])
    return render(request, "dojo_ninjas/index.html", context)    