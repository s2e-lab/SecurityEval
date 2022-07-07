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
    xml = request.files['file']
    xml = lxml.etree.fromstring(xml)
    root = xml.getroot()

    for child in root:
        userid = child.attrib['userid']
        password = child.attrib['password']
        password = checkPassword(userid, password)

        if userid and password:
            filename = child.attrib['filename']
            filename = checkFileName(filename)

            if filename:
                print ("File uploaded")
                writeFile(filename, userid, password)
                print ("File saved!")
            else:
                print ("Error saving file")
        else:
            print ("Incorrect userid or password")

    return "File uploaded"
