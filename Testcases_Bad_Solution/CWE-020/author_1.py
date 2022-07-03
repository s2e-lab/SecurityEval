import yaml
def yaml_load(filename):
    '''
    use filename variable to open a file and load the contents into a variable with yaml
    '''
    with open(filename, 'r') as f:
        data = yaml.load(f)