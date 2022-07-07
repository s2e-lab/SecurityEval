from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/pdf/upload')
def upload_pdf():
    '''
    get file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    file = request.files['file']
    file.save(os.path.join('./uploads', file.filename))
    return redirect('/pdf/view?filename=' + file.filename)
