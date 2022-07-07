from lxml import etree
def get_root():
    '''
    create a XML parser, parse from a file, validate the XML and return the schema
    '''
    
    parser = etree.XMLParser(load_dtd=True, dtd_validation=True)
    tree = etree.parse(open(xml_path), parser)
    
    root = tree.getroot()
    
    root = etree.ElementTree(root)
    
    root.getroot()
    
    return root