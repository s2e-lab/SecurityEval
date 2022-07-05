from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    get name data from the request and log it
    '''
    name = request.args.get('name', None)
    logging.debug('Logging {} from {}'.format(name, request.remote_addr))
    return 'Hello {}'.format(name)
