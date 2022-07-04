def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    print("The number is:", num)
    return
