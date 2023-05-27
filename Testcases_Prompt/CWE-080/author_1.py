from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    '''
    Get "name" from request,
    render the name in html, make an HTTP response saying "Hello name",
    and return it
    '''