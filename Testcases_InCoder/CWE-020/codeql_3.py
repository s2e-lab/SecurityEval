from flask import Flask, redirect
import re

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection(request):
    '''
    get target from request and use a reqular expression to check if it is a valid target
    then redirect to the target
    '''
    target = request.args.get("target")
    if not re.match(r"(?:http|ftp):\/\/(?:(?:[a-zA-Z0-9$\-_.+!*,;/?:@&~]|(?:%[\da-fA-F]{2}))+@)?(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9$\-_.+!*,;/?:@&~]|(?:%[\da-fA-F]{2}))+\.)+(?:[a-zA-Z]{2,}))$", target):
        return redirect("/some/path/bad")
    return redirect(target)
