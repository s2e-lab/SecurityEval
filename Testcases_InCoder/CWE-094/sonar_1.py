from flask import request

@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version by using exec()
    '''
    version = request.args.get("version")
    exec(version)
    return version