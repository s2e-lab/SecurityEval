from flask import Flask
app = Flask(__name__)


import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    call do_computation() method within a try-except block
    in except block, print the traceback of the exception
    '''
    try:
        do_computation()
    except Exception as e:
        traceback.print_exc()
        return 'Error message from server'
    return 'Hello World!'
