from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderhtml")
def renderHTML():
    '''
    get name from request 
    render the name in html to make response and return it
    '''
    name = request.args.get('name')
    html = render_template('template.html', name=name)
    resp = make_response(html)
    resp.headers['Content-Type'] = 'text/html'
    return resp
