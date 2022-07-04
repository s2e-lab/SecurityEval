from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/name')
def name():
    '''
    get name from request and make a response with it and return
    '''
    name = request.args.get('name', '')
    response = make_response('Your name is '+name)
    return response