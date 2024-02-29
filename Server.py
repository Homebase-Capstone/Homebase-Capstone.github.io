import sqlite3
from flask import Flask, request, render_template

# Connect to the database

conn = sqlite3.connect("users.db")
c = conn.cursor()

# Create users table
c.execute("""CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);""")
app = Flask(__name__, template_folder='templates',static_folder='static')

# Add some sample users (optional)
print("test")
conn.commit()
conn.close()
@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "GET":
    return render_template("index.html")
@app.route("/login", methods=["GET", "POST"])
# def login():
#     return render_template("Login.html")
def login():
  if request.method == "GET":
    return render_template("Login.html")
  else:
    # Get username and password from the form
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    username = request.form.get("username")
    password = request.form.get("password")
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    print("test")
    return render_template("index.html") if user else "Login failed!"

@app.route("/register", methods=["GET", "POST"])
def signup():
  if request.method == "GET":
    return render_template("register.html")
  else:
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    username = request.form.get("username")
    password = request.form.get("password")
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return "User created successfully!"

    

if __name__ == "__main__":
    app.run(debug=True)

