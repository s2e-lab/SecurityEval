import xml.sax
def get_root():
    '''
    create a XML parser, handler, feature
    parse from a file and return the result
    '''
 
    handler = xml.sax.make_parser()
    handler.setContentHandler(xml.sax.ContentHandler()) 
    handler.startDocument()
    handler.startElement("root", {})
    handler.endElement("root")
    handler.endDocument()
    return handler.getRootElement()