def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    try:
        a = int(input("Enter an integer > "))
    except ValueError:
        print("Please enter an integer")
        convert_to_int()
    else:
        return a