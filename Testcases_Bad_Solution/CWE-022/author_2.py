import json
import urllib.request as request
def readJSON(url):
    '''
    read a json file from a url using urlopen and return the json object
    '''
    response = request.urlopen(url)
    data = json.loads(response.read())
    return data
