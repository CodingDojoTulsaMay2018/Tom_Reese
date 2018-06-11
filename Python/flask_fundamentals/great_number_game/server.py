from flask import Flask, request, redirect, session, render_template
import random
app=Flask(__name__)
app.secret_key='123'

@app.route('/')
def index():
    reset=""
    # test=session['box_type']
    if 'result' not in session:
        session['result'] = ""
    if 'display' not in session:
        session['display'] = ""
        print(session['display'])
    if 'hide' not in session:
        session['hide'] = "display:none"
    if 'number' not in session:
        result = ""
        session['number'] = str(random.randrange(0,101))
        print("the number is",session['number'])
    else:
        result = session['result']
    if 'style' not in session:
        session['style'] = ""
    print(session['display'])
    
    return render_template('index.html',result=result, reset=reset,style=session['style'], display=session['display'], hide=session['hide'])

@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    session['number'] = int(session['number'])
    if session['guess'] == session['number']:
        print("user guessed the correct number")
        session['style'] = "nailedit"
        session['result'] = 'Great job!  You nailed it!'
        session['display'] = "display:none;"
        session['hide'] = ""
        return redirect('/',)
    if session['guess'] > session['number']:
        session['result'] = "Too High!"
        session['style'] = "toohigh"
        print(session['result'])
        return redirect('/')
    if session['guess'] < session['number']:
        session['result'] = "Too Low!"
        session['style'] = "toolow"
        print(session['result'])
    return redirect('/')

@app.route('/reset',methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)