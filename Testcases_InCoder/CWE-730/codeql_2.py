from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request, comipile it and then use it for search
    '''
    pattern = request.args.get('pattern')
    pattern = re.compile(pattern)
    return render_template('direct.html', pattern=pattern)

