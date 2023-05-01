def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    userInput = int(input("Enter a number: "))
    assert type(userInput) == int
    return userInput

    