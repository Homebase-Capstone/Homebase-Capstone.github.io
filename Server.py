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
app = Flask(__name__, template_folder='templates')

# Add some sample users (optional)
print("test")
conn.commit()
conn.close()
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("Login.html")
# def login():
#     username = request.form["username"]
#     password = request.form["password"]

#     # Connect to database
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()

#     # Check user credentials
#     c.execute("SELECT * FROM users WHERE username = ?", (username,))
#     user = c.fetchone()

#     if not user or password != user[2]:
#         error = "Invalid username or password."
#         return render_template("Login.html", error=error)

#     # Login successful
#     # ... (Implement session management)

#     return "Welcome, " + username + "!"

if __name__ == "__main__":
    app.run(debug=True)

