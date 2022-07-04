from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''
    pattern = request.args.get('pattern')
    if re.search(pattern, "123456789"):
        return "Found"
    else:
        return "Not Found"
