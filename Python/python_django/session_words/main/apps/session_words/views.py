from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    print("user is at index")
    if 'list' not in request.session:
        request.session['list'] = []
    
    context = {
        'list' : request.session['list']
    }
    print(context)
    return render(request, "session_words/index.html", context)

def add_word(request):
    
    if not request.POST['word']:
        return redirect('/')
    else:
        request.session['word'] = request.POST['word']
    if 'color' not in request.POST:
        request.session['color'] = "black"
    else:
        request.session['color'] = request.POST['color']
    if 'big' not in request.POST:
        request.session['big'] = "off"
    else:
        request.session['big'] = request.POST['big']

    request.session['time'] = (f"  -Added on "+strftime("%Y-%m-%d %H:%M %p", gmtime()))

    templist = request.session['list']
    templist.append({
        'word' : request.session['word'], 
        'time' : request.session['time'], 
        'color': request.session['color'], 
        'big': request.session['big']})
    
    request.session['list'] = templist
    
    print("user submitted information")
    return redirect('/')

def clear(request):
    request.session.clear()
    print("user is clearing results")
    return redirect('/')

