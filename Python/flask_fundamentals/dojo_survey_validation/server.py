from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'ThisisSecret'

@app.route('/')
def hello():

    return render_template("index.html")

@app.route('/result')
def results():

    return render_template("result.html", name=session['name'], location=session['location'], lang=session['fav_lang'], comment=session['comment'])

@app.route('/danger',methods=['POST'])
def danger():
    print("user went to danger, all user base are belong to us")
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!")
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!")
    if len(request.form['name']) < 1 or len(request.form['comment']) < 1:
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['dojo_location']
    session['fav_lang'] = request.form['fav_lang']
    session['comment'] = request.form['comment']
    return redirect('/result')

app.run(debug=True)