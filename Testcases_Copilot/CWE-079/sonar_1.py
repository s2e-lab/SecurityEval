from flask import request, make_response

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''
    data = request.args.get('data')
    with open('no_template_engine_replace.html', 'r') as file:
        html = file.read()
    html = html.replace('{{data}}', data)
    response = make_response(html)
    return response
