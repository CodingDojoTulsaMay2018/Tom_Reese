from flask import Flask,request, render_template,redirect,session,flash
from flask_bcrypt import Bcrypt    
# from mysqlconnection import connectToMySQL    
import re, pymysql.cursors



app = Flask(__name__)        
bcrypt = Bcrypt(app)
app.secret_key = 'ThisisSecret'

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def hello():
    print("hello world!")
    return render_template('index.html')

@app.route('/createUser', methods=['POST'])
def create():
    count = 0
    print("testing our flash messages")
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank!")
        count+=1
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank!")
        count+=1
    if request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash("Name cannot have a number in it")
        count+=1
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters!")
        count+=1
    if request.form['password'] != request.form['password_confirm']:
        flash("Password and Password Confirmation do not match!")
        count+=1
    if count >  0:
        print("something went wrong with creating a user")
        return redirect('/')
    # session['first_name'] = request.form['first_name']
    # session['last_name'] = request.form['last_name']
    # session['username'] = request.form['username']
    pw_hash = bcrypt.generate_password_hash(request.form['password'])  
    print(pw_hash)  
    # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'
    # be sure you set up your database so it can store password hashes this long (60 characters)
    query = "INSERT INTO users (username,first_name,last_name, password) VALUES (%(username)s,%(first_name)s,%(last_name)s, %(password_hash)s);"
    # put the pw_hash in our data dictionary, NOT the password the user provided
    data = { "username" : request.form['username'], "first_name" : request.form['first_name'], "last_name" : request.form['last_name'], "password_hash" : pw_hash }
    mysql.query_db(query, data)
    return redirect("/")


@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    query = "SELECT * FROM users WHERE username = %(username)s;"
    data = { "username" : request.form["username"] }
    result = mysql.query_db(query, data)
    if result:
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, for this approach, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            # if we get True after checking the password, we may put the user id in session
            session['userid'] = result[0]['id']
            # never render on a post, always redirect!
            return redirect('/success')
    # if we didn't find anything in the database by searching by username or if the passwords don't match,
    # flash an error message and redirect back to a safe route
    flash("You could not be logged in")
    return redirect("/")

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
                print("Something went wrong", e)
                flash("Username Already Taken")
                return False

def connectToMySQL(db):
    return MySQLConnection(db)
mysql = connectToMySQL('bcrypt')

app.run(debug=True)
