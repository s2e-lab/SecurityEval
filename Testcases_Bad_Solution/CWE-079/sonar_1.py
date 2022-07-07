from flask import request, make_response

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''
    param = request.args.get('param', '')
    html = open('templates/xss_shared.html').read()
    response = make_response(html.replace('{{ name }}', param))
    return response