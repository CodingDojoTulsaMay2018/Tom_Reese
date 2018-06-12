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
    return render_template('index.html',gold=session['gold'],activity=session['activity'])

@app.route('/process',methods=['POST'])
def process():
    time = datetime.datetime.now().strftime("%A %B %Y at %H:%M %p")
    activity = session['activity']
    # reward = session['gold']
    if request.form['action'] == 'farm':
        reward = randint(10,20)
        session['gold']+=reward
        activity.insert(0,("Earned "+str(reward)+" gold from the farm at " + str(time),"color:green;"))
    if request.form['action'] == 'cave':
        reward = randint(5,10)
        session['gold']+=reward
        activity.insert(0,("Earned "+str(reward)+" gold from the cave at " + str(time),"color:green;"))
    print("test")
    if request.form['action'] == 'house':
        reward = randint(2,5)
        session['gold']+=reward
        activity.insert(0,("Earned "+str(reward)+" gold from the house at " + str(time),"color:green;"))
    print("test")
    if request.form['action'] == 'casino':
        print(" is my current gold")
        # if session['gold'] == 0:
        #     activity.insert(0,("You're BROKE!  Go HOME! It's "+ str(time),"color:purple;"))
        # else:
        #     reward = randint(-50,50)
        #     if reward > 0:
        #         activity.insert(0,("Won "+str(reward)+" gold from the casino at "+ str(time),"color:green;"))
        #         session['gold']+=reward
        #     if reward <=0:
        #         if session['gold'] + reward <= 0:
        #             activity.insert(0,("You lost"+str(reward)+"! You lost all your money at the casino! At the specific time/date of "+ str(time),"color:red;"))
        #             session['gold']=0
        #         else:
        #             session['gold']+=reward
        #             activity.insert(0,("Lost "+str(reward)+" gold from the casino at "+ str(time),"color:red;"))
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect ('/')

app.run(debug=True)