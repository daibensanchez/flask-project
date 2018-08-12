from flask import render_template
from controllers import getbook
from app import app
@app.route('/get_book')
#database connection
def get_book():
    return getbook()

@app.route('/')
def hello_world():
    return render_template('hello/index.html')

@app.route('/getbook')
def getbooks():
    booklist = getbook()
    return render_template('hello/getbook.html',data=booklist)

@app.route('/test')
def testlink():
    return render_template('hello/test.html')
'''
@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method=='POST':
        nm=request.form['nm']
        addr=request.form['add']
        city=request.form['city']
        pin=request.form['pin']
        con=sqlite3.connect("database.db")
        cur=con.cursor()
        cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))

    return render_template('hello/addrec.html')
  '''
'''
@app.route('/list')
def list():
    con=sqlite3.connect("database.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from students")
    rows=cur.fetchall()
    return render_template("hello/list.html",rows=rows)
'''