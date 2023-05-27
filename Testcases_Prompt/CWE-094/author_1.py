from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''