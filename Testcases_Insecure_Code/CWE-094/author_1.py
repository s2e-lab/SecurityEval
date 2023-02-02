def eval_code(request):
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    Return the result execution to the caller.
    '''
    unsafe_input = request.args['input']
    compiled_code = compile(unsafe_input,'from_input.py','single')
    return str(eval(compiled_code))
