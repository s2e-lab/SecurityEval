from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderhtml")
def renderHTML():
    '''
    get name from request 
    render the name in html to make response and return it
    '''
    name = request.args.get('name')
    response = make_response(f"<h1>{name}</h1>")
    return response
