from flask import request

@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version by using exec()
    '''
    module_version = request.args.get('module_version')
    exec(f"import urllib{module_version}")
    return "Hello World!"
