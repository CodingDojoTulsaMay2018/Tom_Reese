from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

# Create your views here.




def index(request):
    print("ninja is looking for gold...")
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []

    context = {
        'gold' : request.session['gold'],
        'activity' : request.session['activity']
    }
    return render(request, "ninja_gold/index.html", context)

def process(request):
    print("ninja is processing gold")
    activity = request.session['activity']
    
    time = (f"...",strftime("%Y-%m-%d %H:%M %p", gmtime()))

    print(request.POST['action'])

    if request.POST['action'] == 'farm':
        reward = random.randint(10,20)
        request.session['gold']+=reward
        activity.insert(0,{'activity' : "Earned "+str(reward)+" gold from the farm at" + str(time),'color': 'green'})
    if request.POST['action'] == 'cave':
        reward = random.randint(5,10)
        request.session['gold']+=reward
        activity.insert(0,{'activity' : "Earned "+str(reward)+" gold from the cave at" + str(time), 'color':'green'})
    print("test")
    if request.POST['action'] == 'house':
        reward = random.randint(2,5)
        request.session['gold']+=reward
        activity.insert(0,{'activity' : "Earned "+str(reward)+" gold from the house at" + str(time), 'color' : 'green'})
    print("test")
    if request.POST['action'] == 'casino':
        if request.session['gold'] == 0:
            activity.insert(0,{'activity' : "You're BROKE!  Go HOME! It's "+ str(time),"color":"purple"})
        else:
            reward = random.randint(-50,50)
            if reward > 0:
                activity.insert(0,{'activity' : "Won "+str(reward)+" gold from the casino at "+ str(time),"color":"green"})
                request.session['gold']+=reward
            if reward < 0:
                if request.session['gold'] + reward <= 0:
                    activity.insert(0,{'activity' : "You lost"+str(reward)+"! You lost all your money at the casino! At the specific time/date of "+ str(time),"color":"red"})
                    request.session['gold']=0
                else:
                    request.session['gold']+=reward
                    activity.insert(0,{'activity' : "Lost "+str(reward)+" gold from the casino at "+ str(time),"color":"red"})
            
            
    print("testing went OK")


    request.session['activity'] = activity
    print(request.session['activity'], " is the most currnet activity")
    print("end of processing")
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')


# def index():

# return render_template('index.html',gold=session['gold'],activity=session['activity'])


# def process():

# reward = session['gold']

    
# return redirect('/')
