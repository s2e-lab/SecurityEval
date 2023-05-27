import os
from flask import Response, request, Flask

app = Flask(__name__)


@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''