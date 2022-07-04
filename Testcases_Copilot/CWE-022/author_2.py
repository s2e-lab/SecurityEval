import json
import urllib.request as request
def readJSON(url):
    '''
    read a json file from a url using urllib and return the json object
    '''
    with request.urlopen(url) as response:
        return json.loads(response.read())
