from tempfile import mktemp

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    with open(mktemp(), 'w') as f:
        f.write(results)