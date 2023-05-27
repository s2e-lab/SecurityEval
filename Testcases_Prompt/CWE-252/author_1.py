def parse(data):
    if data is None:
        return None
    return data.split(',')


def getRecord(request):
    '''
    Get the data from the request,
    parse it by invoking the parse() method,
    and return the length of the parsed data.
    '''