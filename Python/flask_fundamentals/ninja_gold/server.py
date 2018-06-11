from flask import Flask, request, redirect, session, render_template
from random import randint 
import datetime, time
app=Flask(__name__)
app.secret_key='1234'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    # if 'color' not in session:
    #     session['color'] = "black"
    return render_template('index.html',gold=session['gold'], activity=session['activity'])

@app.route('/process',methods=['POST'])
def process():
    time = datetime.datetime.now().strftime("%A %B %Y at %H:%M %p")
    activity = session['activity']
    if request.form['action'] == 'farm':
        reward = randint(10,20)
        activity.insert(0,"Earned"+str(reward)+"gold from the farm at " + str(time))
    elif request.form['action'] == 'cave':
        reward = randint(5,10)
        activity.insert(0,"Earned"+str(reward)+"gold from the cave at " + str(time))
    elif request.form['action'] == 'house':
        reward = randint(2,5)
        activity.insert(0,"Earned"+str(reward)+"gold from the house at " + str(time))
    elif request.form['action'] == 'casino' and session['gold'] == 0:
        activity.insert(0,"You got not money, go home, its "+str(time))
    elif request.form['action'] == 'casino':
        if session['gold'] > 0:
            reward = randint(-50,50)
            activity.insert(0,"Earned"+str(reward)+"gold from the casino at "+ str(time))
        if reward-session['gold'] <=0:
            activity.insert(0,"You lost all your money at the casino! At the specific time/date of "+ str(time))
        elif reward < 0:
            activity.insert(0,"Lost"+str(reward)+"gold from the casino at "+ str(time))
            
    session['gold']+=reward
    session['activity']=activity
    return redirect('/')

app.run(debug=True)