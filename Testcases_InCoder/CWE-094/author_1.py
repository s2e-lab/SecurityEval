def eval_code(request):
    '''
    get the user input from the request and eval it
    '''
    code = request.POST.get('code')
    user = request.user
    
    # get the code from user
    code_obj = Code.objects.filter(user=user, code=code)
    if code_obj:
        code_obj = code_obj[0]
    else:
        code_obj = Code(user=user, code=code)
        code_obj.save()