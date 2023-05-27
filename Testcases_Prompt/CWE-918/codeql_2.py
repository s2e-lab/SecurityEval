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