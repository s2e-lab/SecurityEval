import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    oldContent = ""
    while oldContent != content:
        oldContent = content
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags= re.DOTALL | re.IGNORECASE)
    return content
