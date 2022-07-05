from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

'''
run the flask application
'''
if __name__ == "__main__":
    app.run()
