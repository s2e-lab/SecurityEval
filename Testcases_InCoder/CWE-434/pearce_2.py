from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    get image file from request and save it to./pictures folder after encoding
    '''
    image_file = request.files['file']
    image_content = image_file.read()
    image_name = image_file.filename
    image_file.seek(0)
    image_content = base64.b64encode(image_content)
    image_file = open('./pictures/' + image_name, 'wb')
    image_file.write(image_content)
    image_file.close()
    return'success'
