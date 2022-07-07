import logging
def inputConversion():
    '''
    take a string input from the user
    convert it to an integer within try-except block and log the error
    return the user input after converting it to an integer
    '''
    try:
        integer = int(input("Enter an integer: "))
    except ValueError:
        print("That is not a valid integer")
        inputConversion()
    else:
        return integer