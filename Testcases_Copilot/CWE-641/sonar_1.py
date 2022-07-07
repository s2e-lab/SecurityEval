from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    get the file name from the request and parse the name to get the file path
    send the file to the client as attachment
    '''
    file_name = request.args.get('file_name')
    file_path = './' + file_name
    return send_file(file_path, as_attachment=True)
