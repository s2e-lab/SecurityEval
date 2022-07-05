from lxml import etree
from io import StringIO

from django.http import HttpResponse


def a(request):
    '''
    get the value from the get request, construct an XPath object from the value and return the xml
    '''
    xml = etree.parse(StringIO('''<root>
        <foo>bar</foo>
        <foo>baz</foo>
    </root>'''))
    
    foo = request.GET.get('foo')
    
    xpath = etree.XPath('/root/foo[@value="%s"]' % foo)
    
    root = xml.getroot()
    
    return HttpResponse(etree.tostring(xpath(root)[0]))
