import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    pattern = re.compile(r"<script[^>]*?>.*?</script>", re.DOTALL | re.IGNORECASE)
    
    return re.sub(pattern,"",content)

