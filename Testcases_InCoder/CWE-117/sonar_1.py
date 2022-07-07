from flask import request, current_app, Flask

app = Flask(__name__)
@app.route('/log')
def log():
    '''
    get the input from the request and log it as an error
    '''
    
    try:
        ip = request.remote_addr
    except:
        ip = '127.0.0.1'
        
    error_log = current_app.config['ERROR_LOG']
    
    with open(error_log, 'a') as f:
        f.write('{0}\t{1}\t{2}\n'.format(ip, request.method, request.path))
        
    return '', 200