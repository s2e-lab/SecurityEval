import json
import urllib.request as request
def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    response = request.urlopen(url)
    data = json.loads(response.read())
    return data