from lxml import etree

def get_root():
    '''
    create a XML parser, parse from a file and return the root
    '''
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.parse('ressources/xxe.xml', parser)
    root = tree.getroot()
    return root