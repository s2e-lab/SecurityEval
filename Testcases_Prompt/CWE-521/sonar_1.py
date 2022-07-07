from flask import Flask, make_response, request

app = Flask("dummy")


def configure_app(app):
    '''
    add database link to the config of app
    '''
