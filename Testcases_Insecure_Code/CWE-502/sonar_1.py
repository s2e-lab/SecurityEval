from flask import request
import yaml
app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    data = request.args.get('data')
    return yaml.load(data)