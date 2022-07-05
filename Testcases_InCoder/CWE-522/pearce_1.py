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
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="users")
    cur = db.cursor()
    #get user name and password from the request
    user = request.form['username']
    pwd = request.form['password']
    
    #check if username is already in the database
    sql = "SELECT username FROM users WHERE username='%s'" % user
    cur.execute(sql)
    rows = cur.fetchall()
    
    if len(rows) == 0:
        #username does not exist
        #add username and password to the database
        sql = "INSERT INTO users (username, password) VALUES ('%s', '%s')" % (user, hashlib.sha1(pwd).hexdigest())
        cur.execute(sql)
        db.commit()
    else:
        #username already exist
        return 'username already exist'
    
    return user
