from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    
    print("user is at survey")
    return render(request, "survey_form/index.html")

def submit(request):
    print(request.POST)
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['dojo_location']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['comment'] = request.POST['comment']
    print("user submitted information")
    return redirect('/result')

def result(request):
    request.session['count']+=1
    context = {
        'name': request.session['name'],
        'location' : request.session['location'],
        'lang' : request.session['fav_lang'],
        'comment' : request.session['comment'],
        'count' : request.session['count']
    }

    print("user is at results")
    return render(request,'survey_form/result.html', context)

