from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello World!"
@app.route('/play')
def index(): 
    box = "<div class=boxes></div>"
    return render_template("playground.html")+box*3
@app.route('/play/<num>')
def playnum(num):
    multi = int(num)
    box = "<div class=boxes></div>"
    return render_template("playground.html")+box*multi
@app.route('/play/<num>/<color>')
def playnumcolor(num,color):
    multi = int(num)
    background = str(color)
    box = "<div class=boxes style=background-color:"+background+";></div>"
    return render_template("playground.html")+box*multi

if __name__=="__main__":
    app.run(debug=True)