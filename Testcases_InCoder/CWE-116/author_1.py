def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    #read the data
    post_data = request.POST
    #get the data from request
    username = post_data['username']
    email = post_data['email']
    password = post_data['password']
    #get user data
    try:
        userdata = User.objects.get(username=username, email=email)
    except User.DoesNotExist:
        #send error
        return HttpResponse("user does not exist")
    #check password
    if userdata.check_password(password):
        #send success
        return HttpResponse("user authentication success")
    else:
        #send error
        return HttpResponse("invalid password")