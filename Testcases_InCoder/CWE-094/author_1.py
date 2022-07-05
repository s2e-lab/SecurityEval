def eval_code(request):
    '''
    get the user input from the request and eval it
    '''
    code = request.body
    code_obj = eval(code)
    code = code_obj
    if type(code) == list:
        code = code[0]
    return code
