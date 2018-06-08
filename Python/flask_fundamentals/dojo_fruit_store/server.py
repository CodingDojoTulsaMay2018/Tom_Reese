from flask import Flask, render_template, request, redirect, session
import datetime, time 
app = Flask(__name__)  
app.secret_key="12345"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/danger', methods=['POST'])         
def checkout():
    print("user went to danger, all user base are belong to us")
    print("counting items")
    
    # count = int(session['blackberry'])
    session['blackberry'] = request.form['blackberry']
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    return redirect('/checkout')

@app.route('/checkout')         
def orders():
    print("user at orders page")
    count = round(int(session['blackberry'])+int(session['strawberry'])+int(session['raspberry'])+int(session['apple']))
    time= datetime.datetime.now().strftime("%A %B %Y at %H:%M %p")
    # session['name'] = request.form['name']
    return render_template('checkout.html',count=count,apple=session['apple'], blackberry=session['blackberry'], raspberry=session['raspberry'], strawberry=session['strawberry'], first_name=session['first_name'], last_name=session['last_name'], student_id=session['student_id'], time=time)



# @app.route('/danger',methods=['POST'])
# def danger():
#     print("user went to danger, all user base are belong to us")
#     session['name'] = request.form['name']
#     session['location'] = request.form['dojo_location']
#     session['fav_lang'] = request.form['fav_lang']
#     session['comment'] = request.form['comment']
    
#     return redirect('/result')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    