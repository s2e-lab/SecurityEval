import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and return it
    '''
    raw_data = request.args.get("data").encode('utf-8')
    data = base64.decodebytes(raw_data)
    obj = pickle.loads(data)
    return obj