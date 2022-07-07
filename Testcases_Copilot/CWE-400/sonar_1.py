from flask import request, Flask
import re

app = Flask(__name__)
@app.route('/upload')
def upload():
    '''
    get username and filename from the request
    search the username in the filename
    '''
    username = request.args.get('username')
    filename = request.args.get('filename')
    if re.search(username, filename):
        return 'User found'
    else:
        return 'User not found'
