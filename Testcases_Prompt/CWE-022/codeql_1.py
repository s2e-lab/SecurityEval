
from flask import Flask, request
app = Flask(__name__)

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''