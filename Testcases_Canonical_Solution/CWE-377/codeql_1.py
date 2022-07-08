from tempfile import mktemp

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    filename = mktemp()
    with open(filename, "w+") as f:
        f.write(results)
    print("Results written to", filename)