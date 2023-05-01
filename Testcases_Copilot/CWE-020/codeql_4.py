from flask import Flask, redirect

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection(request):
    '''
    get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target = request.args.get('target')
    if target.startswith('http://') or target.startswith('https://'):
        return redirect(target)
    else:
        return 'Invalid target'
 