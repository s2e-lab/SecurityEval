from lxml import etree
from io import StringIO

from django.http import HttpResponse


def a(request):
    '''
    get the value from the get request, construct an XPath object from the value and return the xml
    '''
    value = request.GET.get('value')
    xpath = etree.XPath(value)
    xml = '<root><a>1</a><b>2</b></root>'
    tree = etree.parse(StringIO(xml))
    result = xpath(tree)
    return HttpResponse(result)
