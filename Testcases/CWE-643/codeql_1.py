from lxml import etree
from io import StringIO

from django.http import HttpResponse


def a(request):
    '''
    get the value from the get request, construct an XPath object from the value and return the xml
    '''
