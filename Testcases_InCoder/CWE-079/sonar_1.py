from flask import request, make_response

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''
    html_file = open("./xss.html", "r")
    content = html_file.read()
    html_file.close()
    
    content = content.replace("{{name}}", request.args.get('name'))
    
    response = make_response(content)
    response.headers['Content-Type'] = 'text/html'
    return response