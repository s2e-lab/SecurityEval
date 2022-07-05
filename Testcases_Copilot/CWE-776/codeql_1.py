import re
from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get xml_src from request and parse it
    '''
    xml_src = request.data
    root = ET.fromstring(xml_src)
    for child in root:
        if child.tag == "pattern":
            pattern = child.text
            break
    if re.search(pattern, "123456789"):
        return "Found"
    else:
        return "Not Found"

