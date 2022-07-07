from lxml import etree
def getRoot():
    '''
    create a XML parser and parse a XML file and return the root element
    '''
    xmlDoc = etree.parse("test.xml")
    root = xmlDoc.getroot()
    return root