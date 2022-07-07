from flask import Flask, redirect

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection(request):
    '''
    get target from request and check if it contains a valid domain
    then redirect to the target
    '''
    target = request.args.get('target')
    if target.startswith('http://') or target.startswith('https://'):
        return redirect(target)
    else:
        return 'Invalid target'
 