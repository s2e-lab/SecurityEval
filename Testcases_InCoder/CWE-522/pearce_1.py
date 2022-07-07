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
