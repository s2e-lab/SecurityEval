from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.parse('resources/config.xml', parser)
    root = tree.getroot()
    return root