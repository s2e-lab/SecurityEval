from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Get the file name from the request and parse the name to get the file path
    Send the file to the client as an attachment.
    '''
    file = request.args['file']
    filepath = '/'.join(file.split('_'))
    return send_file(filepath, as_attachment=True)