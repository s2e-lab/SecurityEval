def getFibonacci(n):
    '''
    get n-th fibonacci number using loop
    '''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
