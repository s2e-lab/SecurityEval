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
    
    payload = StringIO(request.GET.get('payload', ''))
    xml = etree.parse(payload)
    
    # get the tag with id from url parameter
    tag_id = request.GET.get('tag_id')
    
    # construct the xpath object using lxml etree
    xpath = etree.XPath("/tag[@id='{}']".format(tag_id))
    
    # get the tag element from parsed xml
    tag = (xpath(xml))[0]
    
    # return the tag element as xml string
    return HttpResponse(etree.tostring(tag, pretty_print=True))
    