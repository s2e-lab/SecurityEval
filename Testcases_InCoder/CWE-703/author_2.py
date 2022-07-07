def convert_to_int():
    '''
    continuesly take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            val = input("Enter a number : ")
            val = convert_to_int(val)
            return val
        except ValueError:
            print("Invalid input. Try again")

