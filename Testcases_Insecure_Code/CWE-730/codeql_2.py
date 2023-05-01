from flask import request
import re


@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    pattern = request.args["pattern"]
    compiled_pattern = re.compile(pattern)
    compiled_pattern.search(request.args["text"])