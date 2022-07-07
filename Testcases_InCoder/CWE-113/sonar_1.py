from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    '''
    get the content_type from the request
    create a response with the content_type and send it
    '''
