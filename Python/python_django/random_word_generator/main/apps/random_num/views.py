from django.shortcuts import render
from django.utils.crypto import get_random_string



def index(request):
    context = {
        'word' : get_random_string(length=14),
    }
    
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter']+=1
    context['count'] = request.session['counter']

    return render(request, "random_num/index.html", context)

def reset(request):
    request.session.clear()
    context = {
        'count' : 0
    }
    return render(request, "random_num/index.html",context)
