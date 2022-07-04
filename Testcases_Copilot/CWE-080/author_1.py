from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderhtml")
def renderHTML():
    '''
    get name from request and render html to response
    '''
    name = request.args.get('name')
    response = make_response(name)
    return response

    