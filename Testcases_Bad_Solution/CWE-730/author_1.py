import re
def checkNumber(number):
    '''
    use regular expression to match lines with numbers
    '''
    pattern = r"/^0\.\d+E?\d+$/"
    if re.match(pattern, number):
        return True
    else:
        return False