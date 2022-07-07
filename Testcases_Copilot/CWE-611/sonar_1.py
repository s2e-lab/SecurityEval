from lxml import etree

def get_root():
    '''
    create a XML parser, parse from a file and return the root
    '''
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse("/home/user/test.xml", parser)
    return tree.getroot()
