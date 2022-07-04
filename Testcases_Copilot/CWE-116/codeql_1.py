import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    return re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)