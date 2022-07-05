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
    userid = request.form.get("userid")
    password = request.form.get("password")
    if checkPassword(userid, password):
        # get the xml file from the request
        xmlFile = request.files.get("xmlFile")
        xmlFileName = xmlFile.filename
        # save the xml file to the server
        xmlFile.save(os.path.join("xml", xmlFileName))
        # get the xml file from server
        xmlFile = os.path.join("xml", xmlFileName)
        # get the user id from the xml file
        xmlDoc = lxml.etree.parse(xmlFile)
        root = xmlDoc.getroot()
        # get all user ids from the xml file
        userids = []
        for child in root:
            if child.tag == "userid":
                userids.append(child.text)
        # check if the userid is in the list
        if userid in userids:
            return xmlFileName
        else:
            return "invalid userid or password"
    else:
        return "invalid userid or password"
