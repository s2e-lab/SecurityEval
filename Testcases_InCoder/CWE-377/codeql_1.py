from tempfile import mktemp

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    temp_file = mktemp()
    with open(temp_file, 'w') as fout:
        json.dump(results, fout)
    return temp_file