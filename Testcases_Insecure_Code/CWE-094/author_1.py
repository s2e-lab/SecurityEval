def eval_code(request):
    '''
    get the user input from the request and eval it
    '''
    unsafe_input = request.args['input']
    return str(eval(unsafe_input))