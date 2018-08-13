from flask import render_template
from controllers import *
from flask import jsonify
from app import app

@app.route('/',methods=['POST','GET'])
def login():
    return render_template("login.html")

@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    rows = getlogin()
    print rows
    if rows != None:
        return render_template('dashboard.html')
    else:
        return render_template("login.html")


@app.route('/getbook',methods=['GET'])
def getbooks():
    booklist = (getbook())
    print((booklist))
    return render_template('hello/getbook.html',book=booklist)

@app.route('/test')
def testlink():
    return render_template('hello/test.html')

@app.route('/users', methods=['GET'])
def getregister():
    return render_template('register.html')

@app.route('/users', methods=['POST'])
def register():
    add_user()
    return render_template('register.html')

@app.route('/users/list',methods=['GET'])
def userslist():
    rows = getusers()
    return render_template("userList.html",rows=rows)
