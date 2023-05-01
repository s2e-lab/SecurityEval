import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args["user_id"]
    url = "https://api.github.com/users/" + user_id
    response = requests.get(url)
    return response.text
