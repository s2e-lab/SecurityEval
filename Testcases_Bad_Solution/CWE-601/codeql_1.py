from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    '''
    get the target url from the request and redirect to it
    '''
    target = request.args.get('target', '')
    return redirect(target, code=302)
