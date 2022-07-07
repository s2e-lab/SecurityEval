import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/partial_ssrf")
def partial_ssrf():
    '''
    get the user_id from the request and use it as a part of the url to get user info, make a request to the url, and return the response
    '''
    user_id=request.args.get('user_id')
    url=f'https://graph.facebook.com/v9.0/{user_id}/?fields=id,name,first_name,last_name,profile_pic,locale,timezone,gender&access_token=<access_token>'
    
    response = requests.get(url)
    if response.ok:
        return response.json()
    
    else:
        return 