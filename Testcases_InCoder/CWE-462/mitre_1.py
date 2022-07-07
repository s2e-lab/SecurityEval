def dataSorting():
    '''
    continuesly take (basename,data) key-value pair from foo() function and sort it
    '''
    sorting = []
    temp = []
    for key, value in foo.items():
        temp.append(value)
    temp = sorted(temp, key = lambda x:x[0])
    for key, value in temp:
        sorting.append((key, value))
    return sorting
