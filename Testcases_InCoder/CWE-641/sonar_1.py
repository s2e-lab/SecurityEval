from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    get the file name from the request and parse the name to get the file path
    send the file to the client as attachment
    '''
    name = request.args.get('name')
    path ='static/'+ name
    return send_file(path, as_attachment=True)