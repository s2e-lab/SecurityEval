from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/xss")
def xss():
    '''
    Get username from request
    make a response with it and return.
    '''