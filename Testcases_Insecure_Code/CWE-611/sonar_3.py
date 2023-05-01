from lxml import etree


def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.parse('resources/config.xml', parser)
    root_xsl = tree.getroot()
    ac = etree.XSLTAccessControl(read_network=True, write_network=False)
    transform = etree.XSLT(root_xsl, access_control=ac)
    return transform
