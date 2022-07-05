import re
def checkNumber(number):
    '''
    use regular expression to match lines with numbers
    '''
    pattern = re.compile('\d+\.*\d*')
    if pattern.match(number):
        return True
    else:
        return False