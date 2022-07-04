def convert_to_int():
    '''
    continuesly take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input")
            continue
        print("The number is:", num)
        break
    return
