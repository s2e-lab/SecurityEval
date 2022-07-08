from flask import request, Response, Flask
app = Flask(__name__)
@app.route('set_location_header')
def set_location_header():
    '''
    get url data from the request and set the location header for redirecting
    '''
    url = request.args["next"]
    response = Response("redirecting...", 302)
    response.headers['Location'] = url  
    return response