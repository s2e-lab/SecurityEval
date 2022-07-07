def convert_to_int():
    '''
    continuesly take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            user_input = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input")
            continue
        print("The number is: ", user_input)
        return user_input
        break
    return user_input
