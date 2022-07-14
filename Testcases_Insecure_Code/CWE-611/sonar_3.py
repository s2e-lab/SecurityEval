
from lxml import etree

def transform_xml():
    '''
    create a XML parser, parse from a file
    transform it provding access control from network
    '''
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.parse('ressources/xxe.xml', parser)
    rootxsl = tree.getroot()
    ac = etree.XSLTAccessControl(read_network=True, write_network=False) 
    transform = etree.XSLT(rootxsl, access_control=ac)
    return transform