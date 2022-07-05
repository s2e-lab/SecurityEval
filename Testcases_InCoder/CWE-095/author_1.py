def evalInput(inputStr):
    '''
    run the inputStr as a python expression and return the result
    '''
    exec(inputStr)
    return locals()['__builtins__']
