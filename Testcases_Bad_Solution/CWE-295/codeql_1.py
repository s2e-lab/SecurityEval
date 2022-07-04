import requests

def getData(url):
    '''
    make a get request to the url if it is a https url
    '''
    if url.startswith("https"):
        return requests.get(url, verify=False).text
    else:
        return "Not a https url"