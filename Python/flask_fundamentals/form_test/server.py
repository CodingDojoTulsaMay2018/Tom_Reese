from flask import Flask, session, render_template, request, redirect
app = Flask(__name__)
app.secret_key="ellasmellslikeroses"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def successs():
    print(request.form)
    return render_template("success.html", name=session['name'],email=session['email'])

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    session['name']=request.form['name']
    session['email']=request.form['email']
    return redirect("/success")

if __name__=="__main__":
    app.run(debug=True) 
