import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/example")
def profile():
    '''
    get raw_data from request with utf-8 encoding and decode it with base64
    load the decoded data with pickle and store it in a variable
    '''
    raw_data = request.args.get('raw_data')
    decoded_data = base64.b64decode(raw_data)
    data = pickle.loads(decoded_data)
    return data
