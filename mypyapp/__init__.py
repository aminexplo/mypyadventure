import flask
from flask import Blueprint
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import Config, TestConfig

bootstrap = Bootstrap()
db = SQLAlchemy()

from .api import bp as api_bp
from .views import bp as main_bp

def create_app(conf):
    app = flask.Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp,url_prefix='/api')
    if conf == 'main':
        app.config.from_object(Config)
    elif conf == 'test':
        app.config.from_object(TestConfig)
    else:
        raise Exception('Invalid configuration token...!')

    db.init_app(app)
    if conf =='test':
        with app.app_context():
            db.create_all()
            
    bootstrap.init_app(app)
    return app
