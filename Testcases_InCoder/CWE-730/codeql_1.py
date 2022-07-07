from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''
    pattern = request.args.get('pattern')
    if pattern:
        matches = re.findall(pattern, request.data)
        return jsonify(matches)
    else:
        return jsonify([])
