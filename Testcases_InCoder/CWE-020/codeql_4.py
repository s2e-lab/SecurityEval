from flask import Flask, redirect

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection(request):
    '''
    get target from request and check if it contains a valid domain
    then redirect to the target
    '''
 
    target = request.get_host()
    
    if target in redirects:
        return redirects[target]
    else:
        return 'Not Found'