def dispatchCommand(command, user, args):
    '''
    this function checks the command data and calls the appropriate function
    when command is 'Login', it calls loginUser()
    when command is 'Retrieve_file', it calls sendFile()
    when command is 'List_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''
    command = command.lower()
    
    #if the command is 'Login', call loginUser()
    if command == 'login':
        loginUser()
        return
    #if the command is 'Retrieve_file', call sendFile()
    elif command =='retrieve_file':
        sendFile()
        return
    #if the command is 'List_files', call listFiles()
    elif command == 'list_files':
        listFiles()
        return
    else:
        print('Invalid Command')
        
    