def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            i = int(input('Enter a number: '))
            return i
        except ValueError:
            print('Sorry you did not enter a valid number')