import logging
def inputConversion():
    '''
    take a string input from the user
    convert it to an integer within try-except block and log the error
    return the user input after converting it to an integer
    '''
    try:
        userInput = input("Enter a number: ")
        userInput = int(userInput)
    except ValueError:
        logging.error("The input was not a number: " + userInput)
    return userInput