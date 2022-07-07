from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''

    pattern = request.args.get('pattern')
    target = request.args.get('target')
    if re.search(pattern, target):
        return "true"
    else:
        return "false"
