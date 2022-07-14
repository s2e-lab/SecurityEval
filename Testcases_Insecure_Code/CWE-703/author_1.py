def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    try:
        user_input = input("Enter a number: ")
        return int(user_input)
    except ValueError:
        pass