import sqlite3
from flask import Flask, request, render_template

# Connect to the database

conn = sqlite3.connect("Houses.db")
c = conn.cursor()

# Create users table
c.execute("""CREATE TABLE IF NOT EXISTS Houses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT NOT NULL UNIQUE,
  stories TEXT NOT NULL
);""")
app = Flask(__name__)