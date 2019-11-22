"""Creates the application"""
from flask import Flask
from flask_pymongo import PyMongo
import mongoengine
from flask_jwt_extended import JWTManager
from flask_cors import CORS


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    # Database
    MONGO_URI = 'mongodb://localhost:27017/'

    # Authentication
    JWT_SECRET_KEY = "enter_secret_here"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    # Database
    DB_NAME = "chef"
    MONGO_URI = f'{BaseConfig.MONGO_URI}{DB_NAME}'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

    # Database
    DB_NAME = "test"
    MONGO_URI = f'{BaseConfig.MONGO_URI}{DB_NAME}'


def create_app(testing=False):

    # CREATE app
    app = Flask(__name__)
    app.config.from_object('config')

    if not testing:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(TestingConfig)

    # CORS
    CORS(app)

    # Create token manager
    JWT = JWTManager(app)

    initialize_extensions(app)

    register_blueprints(app)

    return app

def initialize_extensions(app):
    mongo = PyMongo(app)
    db = app.config['DB_NAME']
    mongoengine.connect(db=db)

def register_blueprints(app):
    from app.routes import auth_routes
    from app.routes import recipe_routes

    app.register_blueprint(auth_routes.AUTH_BP)
    app.register_blueprint(recipe_routes.RECIPE_BP)
