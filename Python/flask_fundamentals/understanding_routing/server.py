from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello World!"

@app.route('/dojo')
def dojohello():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi "+name+"!"

@app.route('/repeat/<num>/<name>')
def repeat(num,name):
    multi = int(num)
    phrase = str(name)
    phrase+=" "
    return phrase*multi

if __name__=="__main__":
    app.run(debug=True)
