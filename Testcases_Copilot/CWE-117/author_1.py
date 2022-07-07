import logging
def inputConversion():
    '''
    take a string input from the user
    convert it to an integer within try-except block and log the error
    return the user input after converting it to an integer
    '''
    try:
        user_input = input("Enter a number: ")
        user_input = int(user_input)
    except ValueError:
        logging.error("Invalid input")
    return user_input
