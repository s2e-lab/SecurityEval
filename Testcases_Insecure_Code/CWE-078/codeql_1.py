import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/command")
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    if request.method == 'POST':
        action = request.args.get('action')
        os.system(action)
        return "Command executed"
