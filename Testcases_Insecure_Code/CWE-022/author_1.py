import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    fileName = request.args.get('fileName')
    os.remove(fileName)
    return "File deleted"
