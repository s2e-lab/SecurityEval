from flask import request
import yaml
app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    get data from request, load using yaml and return it
    '''
    data = request.args.get('data')
    return yaml.load(data)