import tempfile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    f.write(results)
    f.close()
    return f.name
