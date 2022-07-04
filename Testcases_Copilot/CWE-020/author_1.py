import yaml
def yaml_load(filename):
    '''
    use filename variable to open a file and load the contents into a variable with yaml
    '''
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None