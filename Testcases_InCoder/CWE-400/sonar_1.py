from flask import request, Flask
import re

app = Flask(__name__)
@app.route('/upload')
def upload():
    '''
    get username and filename from the request
    search the username in the filename
    '''
