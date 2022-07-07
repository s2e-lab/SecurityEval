from flask import Flask, make_response, request

app = Flask("dummy")


def configure_app(app):
    '''
    add database link to the config of app
    '''
    app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 5
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 20
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 300
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 10
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 10
