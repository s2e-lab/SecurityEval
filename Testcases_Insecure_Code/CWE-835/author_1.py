def getFibonacci(n):
    '''
    Compute the n-th fibonacci number using loops only.
    '''
    a, b = 1, 1
    i = 2
    while i < n:
        a, b = b, a + b
    return b
