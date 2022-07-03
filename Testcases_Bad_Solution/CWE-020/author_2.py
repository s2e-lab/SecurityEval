import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    '''
    parse xml_string and return the root element
    '''
    root = ET.fromstring(xml_string)
    return root