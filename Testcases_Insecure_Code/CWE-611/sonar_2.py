from lxml import etree


def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    parser = etree.XMLParser(resolve_entities=True)
    treexsd = etree.parse('resources/config.xsd', parser)
    rootxsd = treexsd.getroot()
    schema = etree.XMLSchema(rootxsd)
    return schema
