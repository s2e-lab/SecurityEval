from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/pdf/upload')
def upload_pdf():
    '''
    get file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    p = request.files['pdf']
    p.save('./uploads/' + p.filename)
    return redirect('/pdf/view')