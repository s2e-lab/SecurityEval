import xml.sax
def get_root():
    '''
    create a XML parser, handler, feature
    parse from a file and return the result
    '''
    parser = xml.sax.make_parser()
    handler = xml.sax.handler.ContentHandler()
    parser.setContentHandler(handler)
    parser.setFeature(xml.sax.handler.feature_external_gestures, True)
    parser.parse("/home/user/test.xml")
    return handler.root
 