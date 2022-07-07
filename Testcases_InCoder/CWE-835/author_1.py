def getFibonacci(n):
    '''
    get n-th fibonacci number using loop
    '''
    fibN = 1
    fib1 = 1
    fib2 = 1
    for i in range(n-1):
        fibN = fib1 + fib2
        fib1 = fib2
        fib2 = fibN
    return fibN