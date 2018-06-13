from django.shortcuts import render, HttpResponse
from time import gmtime, strftime


def index(request):
    print('at the index')
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print(context)
    return render(request,'time_display/index.html',context)
    