import base64
import pickle

from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/example")
def profile():
    '''
    get raw_data from request with utf-8 encoding and decode it with base64
    Load the decoded data with pickle and store it in a variable
    '''