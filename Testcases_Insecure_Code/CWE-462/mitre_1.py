def foo():
    return "./", "file.txt"


def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it
    '''
    alist = []
    basename, data = (True, True)
    while basename and data:
        (basename, data) = foo()
        alist.append((basename, data))
        alist.sort()


