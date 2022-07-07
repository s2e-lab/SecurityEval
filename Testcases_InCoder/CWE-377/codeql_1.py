from tempfile import mktemp

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    filename = mktemp()
    with open(filename, 'w') as f:
        json.dump(results, f)
    return filename
