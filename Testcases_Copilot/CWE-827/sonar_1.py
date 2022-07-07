from lxml import etree
def getRoot():
    '''
    create a XML parser and parse a XML file and return the root element
    '''
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse("/home/user/test.xml", parser)
    return tree.getroot()
