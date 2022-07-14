from flask import Flask, request
import MySQLdb
import hashlib

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
def register():
    '''
    get username and password from the request, and check if the username is already in the database
    if not, add the username and password to the database after hashing the password
    '''
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone() is not None:
        return "Username already exists"
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        return "Registered successfully"
