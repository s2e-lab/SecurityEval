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
