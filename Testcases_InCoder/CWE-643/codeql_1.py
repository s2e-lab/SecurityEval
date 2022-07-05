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
    if request.GET.get('a'):
        xml = etree.fromstring(
            StringIO('''<tag>
              <id>{}</id>
            </tag>'''.format(request.GET['a'])))
        xpath = etree.XPath("/tag[@id='{}']".format(request.GET['a']))
        print(xpath(xml))
    return HttpResponse('')
