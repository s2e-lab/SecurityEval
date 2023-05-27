from flask import request
import re


@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''