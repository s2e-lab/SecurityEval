def getFibonacci(n):
    '''
    get n-th fibonacci number using loop
    '''
    a,b=1,1
    i = 2
    while i<n:
        a,b=b,a+b
    return b
