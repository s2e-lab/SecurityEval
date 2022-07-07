from lxml import etree
def get_root():
    '''
    create a XML parser, parse from a file, validate the XML and return the schema
    '''
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse("/home/user/test.xml", parser)
    schema = etree.XMLSchema(file="/home/user/test.xsd")
    schema.validate(tree)
    return tree.getroot()
