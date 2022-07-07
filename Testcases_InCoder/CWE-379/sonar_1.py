import tempfile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    #TODO: change this to a temporary file
    file_path = tempfile.NamedTemporaryFile(delete=False).name
    with open(file_path, 'w') as fh:
        json.dump(results, fh, indent=2)
    return file_path
