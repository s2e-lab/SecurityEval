from lxml import etree


def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''