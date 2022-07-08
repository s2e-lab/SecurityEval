from flask import request

@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version by using exec()
    '''

    module = request.args.get("module")
    exec("import urllib%s as urllib" % module)