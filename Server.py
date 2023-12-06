import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
con = sqlite3.connect('account.db')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enternew')
def Signup():
    return render_template('Signup.html')

@app.route('/addrec',methods = ['POST', 'GET'])

def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            with sqlite3.connect("account.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO account (name, email, password) VALUES (?,?,?)",(name,email,password))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html",msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sqlite3.connect("account.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from account")
    rows = cur.fetchall()
    return render_template("list.html",rows = rows)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logincheck',methods = ['POST', 'GET'])

def logincheck():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            with sqlite3.connect("account.db") as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM account WHERE email=? AND password=?",(email,password))
                con.commit()
                msg = "Login successfully"
        except:
            con.rollback()
            msg = "error in login operation"
        finally:
            return render_template("index.html",msg = msg)
            con.close()

if __name__ == '__main__':
    app.run(debug=True)