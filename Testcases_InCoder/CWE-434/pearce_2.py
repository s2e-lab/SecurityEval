from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    get image file from request and save it to ./pictures folder after encoding
    '''
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('./pictures', filename))
        encoded = base64.encodestring(open(os.path.join('./pictures', filename), 'rb').read())
        return '<img src="data:image/jpeg;base64,{}"/>'.format(encoded.decode())
    else:
        return 'Invalid file'
