import yaml
def yaml_load(filename):
    '''
    use filename variable to open a file
    load the contents into a variable with yaml and retrun it
    '''
    with open(filename, 'r') as file:
        data = yaml.load(file)
    return data
