from flask import Flask, make_response, request

app = Flask("Leak password")

@app.route('/')
def index():
    '''
    get the password from the request, make a response with setting cookies, and return the response
    '''
