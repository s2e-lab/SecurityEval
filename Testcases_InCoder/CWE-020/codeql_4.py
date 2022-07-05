from flask import Flask, redirect

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection(request):
    '''
    get target from request and check if it contains a valid domain
    then redirect to the target
    '''
    target = request.args.get("target")
    if not target or target.startswith("http://") or target.startswith("https://"):
        return redirect("https://" + target)
    else:
        return "Target is invalid"