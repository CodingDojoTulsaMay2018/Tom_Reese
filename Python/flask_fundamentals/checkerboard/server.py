from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("index.html")
@app.route('/<num1>/<num2>')
def customboard(num1,num2):
    multi1 = int(num1)
    multi2 = int(num2)
    css1 = str(num1)
    css2 = str(num2)
    row1 = "<div class=box1></div><div class=box2></div>"
    row2 = "<div class=box2></div><div class=box1></div>"
    setup1 = row1*(int(multi1/2))
    setup2 = row2*(int(multi1/2))
    board = setup1+setup2
    return render_template("index.html",css1=css1)+board*(int(multi1/2))


if __name__=="__main__":
    app.run(debug=True)