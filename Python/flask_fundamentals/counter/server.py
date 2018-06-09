from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key="4567"


@app.route('/')
def hello():
    if 'count' not in session:
        print('session count = 1')
        session['count'] = 1
    else:
        print("doing awesomesauce conversion")
        number = int(session['count'])
        number+=2
        print(number,"is the current number")
        session['count']= str(number)
    print(session['count'],"is the session count")
    total = session['count']
    return render_template("index.html", total=total)

@app.route('/add2', methods=['POST'])
def add2():
    print('user decided to add two to the count')
    return redirect('/')
    
@app.route('/destroy', methods=['POST'])
def destroy_session():
    print('user requested to reset count to 0')
    session.clear()
    print('session count back down to 0')
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    