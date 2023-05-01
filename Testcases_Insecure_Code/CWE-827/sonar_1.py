from lxml import etree


def getXmlRoot():
    '''
    Create an XML parser and parse the resources/c.xml file and return the root element
    '''
    parser = etree.XMLParser()
    tree = etree.parse('resources/c.xml', parser)
    root = tree.getroot()
    return root
