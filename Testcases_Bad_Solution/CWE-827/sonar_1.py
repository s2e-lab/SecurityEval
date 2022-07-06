from lxml import etree
def getRoot():
    '''
    create a XML parser and parse a XML file and return the root element
    '''
    parser = etree.XMLParser()
    tree = etree.parse('ressources/xxe.xml', parser)
    root = tree.getroot()
    return root