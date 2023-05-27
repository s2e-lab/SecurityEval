from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    '''
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''