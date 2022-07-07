def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    print("The number is: ", user_input)
    return user_input
