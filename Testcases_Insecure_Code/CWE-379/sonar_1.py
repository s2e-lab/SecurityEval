import tempfile


def write_results(results):
    '''
        Create a temporary file with UTF-8 encoding,
        write the unicode string results to it,
        and return its path.
    '''
    filename = tempfile.mktemp()
    tmp_file = open(filename, "w+")
    tmp_file.write(results.encode("utf-8"))
    return tmp_file
