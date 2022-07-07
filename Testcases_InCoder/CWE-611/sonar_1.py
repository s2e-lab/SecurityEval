from lxml import etree

def get_root():
    '''
    create a XML parser, parse from a file and return the root
    '''
    root = etree.parse(open('./data/test.xml', 'r')).getroot()
    return root
