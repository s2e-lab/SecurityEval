import json
import urllib.request as request
def readJSON(url):
    '''
    read a json file from a url using urllib and return the json object
    '''
    req = request.Request(url)
    response = request.urlopen(req)
    return json.loads(response.read().decode("utf-8"))
