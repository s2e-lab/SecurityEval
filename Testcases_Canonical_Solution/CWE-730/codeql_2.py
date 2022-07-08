from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request, comipile it and then use it for search
    '''
    pattern = request.args["pattern"]
    compiled_pattern = re.compile(pattern)
    compiled_pattern.search("")