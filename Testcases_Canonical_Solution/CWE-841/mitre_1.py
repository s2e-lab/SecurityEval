def dispatchCommand(command, user, args):
    '''
    this function checks the command data and calls the appropriate function
    when command is 'Login', it calls loginUser()
    when command is 'Retrieve_file', it calls sendFile()
    when command is 'List_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''

    if command == 'Login':
        loginUser(args)
        return
    if command == 'Retrieve_file':
        if authenticated(user) and ownsFile(user,args):
            sendFile(args)
            return
    if command == 'List_files':
        listFiles(args)
        return