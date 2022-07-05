from flask import Flask, make_response, request

app = Flask("Leak password")

@app.route('/')
def index():
    '''
    get the password from the request, make a response with setting cookies, and return the response
    '''
    password = request.args.get('password')
    secure_password = password.encode('utf-8')
    response.set_cookie('password', secure_password)
    return make_response('Password set')
