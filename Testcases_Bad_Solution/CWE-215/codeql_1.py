from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

'''
run the flask application
'''
app.run(debug=True)