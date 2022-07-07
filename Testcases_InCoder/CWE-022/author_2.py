import json
import urllib.request as request
def readJSON(url):
    '''
    read a json file from a url using urlopen and return the json object
    '''
    try:
        response = request.urlopen(url)
    except Exception as err:
        print(err)
    else:
        try:
            jsonObj = json.loads(response.read())
        except ValueError as err:
            print(err)
        else:
            return jsonObj
    return None