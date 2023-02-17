from flask import Flask, redirect, request
import re

app = Flask(__name__)


@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    target = request.args.get('target')
    regex = re.compile("(www|beta).example.com/")
    if regex.match(target):
        return redirect(target)
    else:
        return "Invalid target"
