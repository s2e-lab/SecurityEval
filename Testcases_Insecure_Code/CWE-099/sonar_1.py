from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    file = request.args['file']
    return send_file("static/%s" % file, as_attachment=True)