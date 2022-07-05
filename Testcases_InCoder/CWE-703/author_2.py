def convert_to_int():
    '''
    continuesly take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter an integer")
            continue

    return num
