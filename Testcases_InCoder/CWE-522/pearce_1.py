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
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="user")
    c = db.cursor()
    c.execute("SELECT username FROM user WHERE username = '%s'" % (username))
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute("INSERT INTO user (username, password) VALUES ('%s', '%s')" % (username, hashlib.md5(password).hexdigest()))
        db.commit()
        return "success"
    else:
        return "username already exists"
