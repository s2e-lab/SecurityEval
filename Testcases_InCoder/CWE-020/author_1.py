import yaml
def yaml_load(filename):
    '''
    use filename variable to open a file and load the contents into a variable with yaml
    '''
    stream = open(filename,'r')
    data = yaml.load(stream)
    stream.close()
    return data