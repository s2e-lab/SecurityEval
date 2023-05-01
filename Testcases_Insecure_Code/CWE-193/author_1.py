def incrementByOne(arr):
    '''
    Given an array of integers "arr", increment each of its elements by 1
    '''
    i = 0
    while i <= len(arr):
        arr[i] += 1
        i += 1
    return arr
