from lxml import etree
def get_root():
    '''
    create a XML parser, parse from a file, validate the XML and return the schema
    '''
    parser = etree.XMLParser(resolve_entities=True)
    treexsd = etree.parse('ressources/xxe.xsd', parser)
    rootxsd = treexsd.getroot()
    schema = etree.XMLSchema(rootxsd)
    return schema

