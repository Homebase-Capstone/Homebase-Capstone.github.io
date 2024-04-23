import sqlite3
from flask import Flask, request, render_template, redirect , url_for, json
from flask_cors import CORS


# Connect to the database

conn = sqlite3.connect("users.db")
c = conn.cursor()

# Create users table
c.execute("""CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);""")
app = Flask(__name__)
cors = CORS(app)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = json.loads(request.data.decode('utf-8'))['username'] 
        # Get the username and password from the request form.
        password = json.loads(request.data.decode('utf-8'))['password']
        print(username, password)
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        # Here you would typically check the credentials against a database or other authentication mechanism.
        # For this example, we'll just check if the username and password match a hardcoded value.
        if username == 'admin' and password == 'password':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials')
    else:
        return render_template('login.html') if user else "Login failed!" 

# Home page

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
