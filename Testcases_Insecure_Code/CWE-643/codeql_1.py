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
    value = request.GET['xpath']
    f = StringIO('<foo><bar></bar></foo>')
    tree = etree.parse(f)
    r = tree.xpath("/tag[@id='%s']" % value)