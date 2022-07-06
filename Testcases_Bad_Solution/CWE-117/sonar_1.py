from flask import request, current_app, Flask

app = Flask(__name__)
@app.route('/log')
def log():
    '''
    get the input from the request and log it as an error
    '''
    input = request.args.get('input')
    current_app.logger.error("%s", input)