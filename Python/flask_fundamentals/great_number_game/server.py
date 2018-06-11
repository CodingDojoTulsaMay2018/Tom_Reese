from flask import Flask, request, redirect, session, render_template
import random
app=Flask(__name__)
app.secret_key='123'

@app.route('/')
def index():
    reset=""
    test=session['box_type']
    if 'result' not in session:
        session['result'] = ""
    if 'number' not in session:
        result = ""
        session['number'] = str(random.randrange(0,101))
        print("the number is",session['number'])
    else:
        result = session['result']
    return render_template('index.html',result=result, reset=reset,test=test)

@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    session['number'] = int(session['number'])
    if session['guess'] == session['number']:
        print("user guessed the correct number")
        session['result'] = 'Great job!  You nailed it!'
        session['box_type'] = "display:flex;position;relative:background-color:green;font-size:3em;text-align:center;"
        return redirect('/',)
    if session['guess'] > session['number']:
        session['result'] = "Too High!"
        session['box_type'] = "display:flex;position;relative:background-color:red;font-size:3em;text-align:center;"
        print(session['result'])
        session.pop('guess')
        return redirect('/')
    if session['guess'] < session['number']:
        session['result'] = "Too Low!"
        print(session['result'])
        session['box_type'] = "display:flex;position;relative:background-color:red;font-size:3em;text-align:center;"
        session.pop('guess')
    return redirect('/')

app.run(debug=True)