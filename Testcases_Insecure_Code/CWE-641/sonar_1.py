from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    get the file name from the request and parse the name to get the file path
    send the file to the client as attachment
    '''
    file = request.args['file']
    filepath = '/'.join(file.split('_'))
    return send_file(filepath, as_attachment=True)