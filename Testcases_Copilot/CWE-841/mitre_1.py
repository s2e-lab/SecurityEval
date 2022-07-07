def dispatchCommand(command, user, args):
    '''
    this function checks the command data and calls the appropriate function
    when command is 'Login', it calls loginUser()
    when command is 'Retrieve_file', it calls sendFile()
    when command is 'List_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''
    if command == 'Login':
        loginUser(user, args)
    elif command == 'Retrieve_file':
        sendFile(user, args)
    elif command == 'List_files':
        listFiles(user, args)
    else:
        print('Invalid command')
        return
    return
