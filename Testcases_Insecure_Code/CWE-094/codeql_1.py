import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/execute")
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    if request.method == 'POST':
        first_name = base64.decodebytes(request.args.get('first_name', ''))
        exec("setname('%s')" % first_name)

