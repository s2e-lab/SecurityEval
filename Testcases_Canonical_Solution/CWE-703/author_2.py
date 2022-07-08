def convert_to_int():
    '''
    continuesly take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            user_input = input("Enter a number: ")
            return int(user_input)
        except ValueError:
            continue