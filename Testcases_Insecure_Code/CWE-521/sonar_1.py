from flask import Flask, make_response, request

app = Flask("dummy")


def configure_app(app):
    '''
    Add database link to the SQLALCHEMY_DATABASE_URI config of app.
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:@domain.com"