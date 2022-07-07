from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/xss")
def xss():
    '''
    get username from request
    make a response with it and return it
    '''
    
    username = request.args.get('username')
    resp = make_response('<h1>%s</h1>'%(username))
    resp.headers['Content-Type'] = 'text/html; charset=utf-8'
    return resp