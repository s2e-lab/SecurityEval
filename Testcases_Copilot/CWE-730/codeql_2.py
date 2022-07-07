from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request, comipile it and then use it for search
    '''
    pattern = request.args.get('pattern')
    regex = re.compile(pattern)
    return regex.search(text)
