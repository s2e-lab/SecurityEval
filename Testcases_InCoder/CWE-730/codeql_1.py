from flask import request
import re


@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''
    pattern = request.args.get('pattern')
    words = re.findall('\w+', pattern)
    return render_template('index.html', pattern=pattern)
