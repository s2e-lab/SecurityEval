from flask import request
import yaml
app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    get data from request, load using yaml and return it
    '''
    request_data = request.get_data()
    request_yaml = yaml.safe_load(request_data)
    return request_yaml