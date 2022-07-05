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
    id = request.GET.get('id')
    xml = '<tag id="{}">'.format(id)
    xml += '</tag>'
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(StringIO(xml), parser)
    xpath = etree.XPath('/tag[@id={}]'.format(id))
    result = xpath(tree)
    return HttpResponse(str(result))