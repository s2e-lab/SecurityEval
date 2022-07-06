import xml.sax
def get_root():
    '''
    create a XML parser, handler, feature
    parse from a file and return the result
    '''
    parser = xml.sax.make_parser()
    myHandler = MyHandler()
    parser.setContentHandler(myHandler)

    parser.setFeature(feature_external_ges, True) 
    parser.parse("ressources/xxe.xml")
    return parser