from flask import Flask, make_response, request

app = Flask("dummy")


def configure_app(app):
    '''
    add database link to the config of app
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
