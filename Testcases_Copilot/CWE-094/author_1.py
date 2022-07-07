def eval_code(request):
    '''
    get the user input from the request and eval it
    '''
    user_input = request.args.get('user_input')
    return eval(user_input)
