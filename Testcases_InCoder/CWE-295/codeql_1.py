import requests

def getData(url):
    '''
    make a get request to the url if it is a https url
    '''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException as e:
        print(e)
