import logging
def inputConversion():
    '''
    take a string input from the user
    convert it to an integer within try-except block and log the error
    return the user input after converting it to an integer
    '''
    while True:
        try:
            int_value = int(input('Please input a number: '))
            return int_value
        except ValueError:
            logging.error('Please input a number')