import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    soup = BeautifulSoup(content)
    scripts = soup.findAll('script')
    for script in scripts:
        script.extract()
    return str(soup)