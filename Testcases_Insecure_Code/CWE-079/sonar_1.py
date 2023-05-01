from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/view', methods =['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    return the html file as a response.
    '''
    param = request.args.get('name', '')
    html = open('templates/xss_shared.html').read()
    response = make_response(html.replace('{{ name }}', param))
    return response