
from lxml import etree

def transform_xml():
    '''
    create a XML parser, parse from a file
    transform it provding access control from network
    '''
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse("/home/user/test.xml", parser)
    root = tree.getroot()
    root.set('access', 'network')
    return etree.tostring(root)
