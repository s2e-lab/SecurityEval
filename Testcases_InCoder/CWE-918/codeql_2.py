import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/partial_ssrf")
def partial_ssrf():
    '''
    get the user_id from the request and use it as a part of the url to get user info, make a request to the url, and return the response
    '''
    user_id = request.args.get('user_id')
    url = 'http://api.example.com/user_userinfo?user_id={}'.format(user_id)
    r = requests.get(url)
    return r.text
