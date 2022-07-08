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
    name = request.args.get('name')
    app.logger.info('User name: ' + name) 