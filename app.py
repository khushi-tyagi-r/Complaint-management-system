
from flask import Flask, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(host="localhost", user="root", password="", database="complaint_db")
cursor = db.cursor()

# Create tables if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
cursor.execute("CREATE TABLE IF NOT EXISTS complaints (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, msg TEXT, status VARCHAR(20) DEFAULT 'pending', FOREIGN KEY(user_id) REFERENCES users(id))")

@app.route('/')
def home():
    return "<h2>Complaint System</h2><form action='/add' method='post'>Name:<br><input name='name'><br>Complaint:<br><textarea name='msg'></textarea><br><button>Submit</button></form>"

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    msg = request.form['msg']
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    user_id = cursor.lastrowid
    cursor.execute("INSERT INTO complaints (user_id, msg) VALUES (%s, %s)", (user_id, msg))
    db.commit()
    return "<h3>Submitted to MySQL!</h3><a href='/'>Back</a>"

app.run()
