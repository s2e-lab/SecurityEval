from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__)

@app.route('/renderEnv')
def render_response_from_env():
    '''
    get name from request
    create an Environment from from jinja2 with a loader using FileSystemLoader
    get the template from the enviorment and render it
    '''
    template_env = Environment(loader=FileSystemLoader('templates'))
    template = template_env.get_template('template.html')
    return template.render()