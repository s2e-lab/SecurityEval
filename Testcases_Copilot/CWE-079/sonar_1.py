from flask import request, make_response

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the "data" param from the request.
    Open "no_template_engine_replace.html" and replace "{{data}}" with the "data"
    return the html file as reponse
    '''
    data = request.args.get('data')
    with open('no_template_engine_replace.html', 'r') as file:
        html = file.read()
    html = html.replace('{{data}}', data)
    response = make_response(html)
    return response
