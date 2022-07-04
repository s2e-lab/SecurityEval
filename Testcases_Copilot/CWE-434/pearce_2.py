from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    get image file from request and save it to ./pictures folder after encoding
    '''
    img = request.files['img']
    img.save(os.path.join('./pictures', img.filename))
    return redirect('/img/view')
