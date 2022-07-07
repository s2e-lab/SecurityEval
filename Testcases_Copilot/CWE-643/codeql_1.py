from lxml import etree
from io import StringIO

from django.http import HttpResponse


def a(request):
    '''
    get the value from the get request
    constract the xml payload using StringIO
    parse the xml payload
    construct an XPath object for /tag[@id={}] format from the parsed xml
    '''
    id = request.GET['id']
    xml_src = '<tag id="{}">'.format(id)
    xml_payload = StringIO(xml_src)
    tree = etree.parse(xml_payload)
    xpath = etree.XPath('/tag[@id={}]'.format(id))
    return HttpResponse(xpath(tree))