"""Creates the application"""
import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    # Authentication
    JWT_SECRET_KEY = "enter_secret_here"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = "mongodb://localhost:27017/fork?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


class ProductionConfig(BaseConfig):
    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = os.environ.get('MONGODB_URI')
    if MONGO_URI:
        MONGO_URI = MONGO_URI + "?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


class TestingConfig(BaseConfig):
    TESTING = True

    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = "mongodb://localhost:27017/fork_test?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


def create_app(testing=False):

    # CREATE app
    app = Flask(__name__)

    if testing:
        app.config.from_object(TestingConfig)
    elif os.environ.get('MONGODB_URI'):
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    initialize_extensions(app)

    register_blueprints(app)

    return app

def initialize_extensions(app):# CORS
    # Create token manager
    CORS(app)
    JWT = JWTManager(app)
    mongo = PyMongo(app)
    db = MongoEngine(app)

def register_blueprints(app):
    from app.routes import auth_routes
    from app.routes import recipe_routes

    app.register_blueprint(auth_routes.AUTH_BP)
    app.register_blueprint(recipe_routes.RECIPE_BP)
