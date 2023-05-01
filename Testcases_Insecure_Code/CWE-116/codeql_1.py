import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    oldContent = ""
    while oldContent != content:
        oldContent = content
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    return content

