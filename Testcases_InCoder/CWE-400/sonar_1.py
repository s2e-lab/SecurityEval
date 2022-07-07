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
    
    #get the filename and username
    username_regex = re.compile("[0-9]{8}_[0-9]{8}") 
    filename_regex = re.compile("[0-9]{8}_[A-Z]{2}") 
    
    #search the username and filename in the filename
    if username_regex.match(filename):
        filename = filename_regex.match(filename)
        
        
    return render_template('upload.html', username=username, filename=filename)