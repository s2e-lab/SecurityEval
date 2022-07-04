from flask import request
import yaml
app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    get data from request and load using yaml
    '''
    data = request.args.get('data')
    return yaml.load(data)