from flask import Flask,request, render_template,redirect,session,flash
from flask_bcrypt import Bcrypt    
# from mysqlconnection import connectToMySQL    
import re, pymysql.cursors

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)        
bcrypt = Bcrypt(app)
app.secret_key = 'ThisisSecret'

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',user = 'root',password = 'root', db = db,charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor,autocommit = True)
        self.connection = connection
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("An error is being thrown from the database", e)
                flash("Email address is already being used, enter another email")
                return False

@app.route('/')
def hello():
    print("hello world!")    
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def validate():
    count = 0
    print("testing our email submission for any problems")
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        count+=1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        count+=1
    if count >  0:
        print("something went wrong with creating a new email entry")
        return redirect('/')
    if count > 0:
        print("email registration had a problem during validation")
    print(request.form['email'])
    query = "SELECT email FROM email_list WHERE email = '"+request.form['email']+"';"
    data = mysql.query_db(query)
    if data:
        print("server side found a duplicate email on the database called"+request.form['email'])
        flash("Duplicate Email Address!")
        return redirect('/')
    query = "INSERT INTO email_list (email) VALUES (%(email)s);"
    data = { "email" : request.form['email'] }
    mysql.query_db(query, data)
    flash("The email address you entered "+request.form['email']+" is a VALID email address! Thank you!")
    return redirect("/success")

@app.route('/success')
def success():
    print("user at success page")    
    query = "SELECT * FROM email_list;"
    emails = mysql.query_db(query)
    return render_template('success.html', emails=emails)

@app.route('/erase/<id>',methods=['POST'])
def erase(id):
    print("user at delete page")   
    query = "DELETE FROM email_list WHERE id_email_addresses = '"+id+"';"
    mysql.query_db(query)
    print(id,"has been deleted")
    return redirect('/success')

def connectToMySQL(db):
    return MySQLConnection(db)
mysql = connectToMySQL('email')


app.run(debug=True)
