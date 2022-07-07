import re
def checkNumber(number):
    '''
    use regular expression to match lines with numbers
    '''
    try:
        re.compile("^\d+$")
        return bool(re.match(re.compile("^\d+$"), number))
    except:
        return False
