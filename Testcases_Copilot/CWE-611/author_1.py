from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    pass

@app.post("/upload")
def upload():
    '''
    get the xml file from the request and check if the userid and password are correct
    '''
    xml = request.files['xml']
    tree = lxml.etree.parse(xml)
    userid = tree.xpath('/user/userid/text()')[0]
    password = tree.xpath('/user/password/text()')[0]
    if checkPassword(userid, password):
        return "OK"
    else:
        return "ERROR"
