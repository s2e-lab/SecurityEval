def inputInt():
    '''
    take an int input and return it after checking type
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
