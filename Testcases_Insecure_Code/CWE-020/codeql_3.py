from flask import Flask, redirect
import re

app = Flask(__name__)


@app.route('/redirect')
def redirectToTarget(request):
    '''
    get target URL from request,
    use a reqular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    target = request.args.get('target')
    regex = re.compile("(www|beta).example.com/")
    if regex.match(target):
        return redirect(target)
