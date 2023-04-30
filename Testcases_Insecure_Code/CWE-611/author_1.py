from flask import Flask, request
import lxml.etree

app = Flask(__name__)


def checkPassword(userid, password):
    pass


@app.post("/upload")
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    xml = request.files['xml']
    root = lxml.etree.fromstring(xml.read())
    userid = root.find('userid').text
    password = root.find('password').text
    if checkPassword(userid, password):
        return "OK"
    else:
        return "ERROR"
