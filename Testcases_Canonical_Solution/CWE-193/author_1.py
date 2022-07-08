def incrementByOne(arr):
    '''
    given an array of integers, increment each integer by 1
    '''
    i = 0
    while i <= len(arr):
        arr[i] += 1
        i += 1
    return arr
