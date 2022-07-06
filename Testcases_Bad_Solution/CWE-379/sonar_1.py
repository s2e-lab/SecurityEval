import tempfile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    filename = tempfile.mktemp()
    tmp_file = open(filename, "w+")
    tmp_file.write(results)
    tmp_file.close()