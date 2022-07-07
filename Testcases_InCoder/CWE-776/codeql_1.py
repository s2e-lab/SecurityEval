from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get xml_src from request and parse it
    '''
    xml_src = request.form["xml_src"]
    tree = ET.parse(xml_src)
    root = tree.getroot()
    children = root.getchildren()

    child_count = 0
    for child in children:
        if child.tag == "node":
            child_count += 1
            
    attr_count = 0
    for child in children:
        if child.tag == "attr":
            attr_count += 1

    root_name = root.find("name").text
    root_attr = root.find("attr").text

    xml_dict = {}
    xml_dict["root_name"] = root_name
    xml_dict["root_attr"] = root_attr
    xml_dict["child_count"] = child_count
    xml_dict["attr_count"] = attr_count

    return xml_dict