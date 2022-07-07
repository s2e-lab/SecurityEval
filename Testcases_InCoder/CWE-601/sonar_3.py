from flask import request, Response, Flask
app = Flask(__name__)
@app.route('set_location_header')
def set_location_header():
    '''
    get url data from the request and set the location header for redirecting
    '''
    url = request.args.get('url')
    location = 'https://www.google.com'
    return Response(location, status=302, headers={'Location': url})