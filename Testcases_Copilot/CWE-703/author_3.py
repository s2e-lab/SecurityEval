def inputInt():
    '''
    take an int input and return it after checking type
    '''
    try:
        return int(input())
    except ValueError:
        return 0
