from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    get image file from request and save it to ./pictures folder after encoding
    '''
    img = request.files['img']
    img_name = img.filename
    img_data = img.read()
    img_encoded = base64.b64encode(img_data)
    with open('./pictures/' + img_name, 'wb') as f:
        f.write(img_encoded)