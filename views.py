from flask import render_template
from controllers import *
from flask import jsonify
from app import app

@app.route('/',methods=['POST','GET'])
def login():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/getbook',methods=['GET'])
def getbooks():
    booklist = getbook()
    print((booklist))
    return render_template('hello/getbook.html',book=booklist)



@app.route('/users', methods=['GET'])
def getregister():
    return render_template('register.html')

@app.route('/genre', methods=['GET'])
def getgenre():
    #genres = get_genres()
    return render_template('dispCat_all.html',genres=genres)

@app.route('/users', methods=['POST'])
def register():
    adduser()
    return render_template('register.html')

@app.route('/userList',methods=['GET'])
def userslist():
    rows = getusers()
    return render_template("userList.html",rows=rows)