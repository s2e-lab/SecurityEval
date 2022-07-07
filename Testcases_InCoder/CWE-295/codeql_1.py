import requests

def getData(url):
    '''
    make a get request to the url if it is a https url
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()
    except:
        print('Error while getting data from', url)
        raise
    return r.text