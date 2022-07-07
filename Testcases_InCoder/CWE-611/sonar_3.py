
from lxml import etree

def transform_xml():
    '''
    create a XML parser, parse from a file
    transform it provding access control from network
    '''
    tree = etree.parse("test.xml")
    root = tree.getroot()
    xml = etree.tostring(root,pretty_print=True)