from tempfile import mktemp

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    fd = open(mktemp(), 'w')
    fd.write(results)
    fd.close()
    return fd.name
