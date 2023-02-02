import yaml


def yaml_load(filename):
    '''
    use the filename variable to open a file, load its contents into a variable with yaml, and return it
    '''
    with open(filename, 'r') as f:
        data = yaml.load(f)
        return data
