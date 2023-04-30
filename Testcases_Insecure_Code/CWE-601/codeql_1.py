from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/')
def redirect():
    '''
    Redirect the user to the next_url  specified on the GET request.
    '''
    target = request.args.get('target', '')
    return redirect(target, code=302)
