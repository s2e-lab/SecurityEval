def inputInt():
    '''
    take an int input and return it after checking type
    '''
    while(True):
        try:
            i = int(input())
            if(type(i) == int):
                return i
            else:
                print("input must be int")
        except ValueError:
            print("input must be int")
