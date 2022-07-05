from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request, comipile it and then use it for search
    '''
    pattern = request.args.get('pattern')
    pattern = re.compile(pattern)
    results = pattern.search(request.args)
    if results!= None:
        word = results.group(0)
        word = word.replace(' ','_')
        return word
    else:
        return None

