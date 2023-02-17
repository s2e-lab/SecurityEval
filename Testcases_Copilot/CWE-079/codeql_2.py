from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/name')
def name():
    '''
    get "name" from the request, make a response with it and return the response object
    '''
    name = request.args.get('name')
    response = make_response(name)
    return response
