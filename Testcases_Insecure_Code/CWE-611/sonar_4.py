import xml.sax
def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    parser = xml.sax.make_parser()
    myHandler = MyHandler()
    parser.setContentHandler(myHandler)

    parser.setFeature(feature_external_ges, True) 
    parser.parse("resources/config.xml")
    return parser