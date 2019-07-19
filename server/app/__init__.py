"""Creates the application"""
from flask import Flask
from flask_pymongo import PyMongo
import mongoengine
from flask_jwt_extended import JWTManager

# CREATE app
APP = Flask(__name__)
APP.config.from_object('config')
APP.config.from_pyfile(filename='..\\instance\\config.py')

# Create token manager
JWT = JWTManager(APP)

# CREATE database
MONGO = PyMongo(APP)
mongoengine.connect(db=APP.config['DB_NAME'])

from app.routes import auth_routes
APP.register_blueprint(auth_routes.AUTH_BP)
from app.routes import recipe_routes
APP.register_blueprint(recipe_routes.RECIPE_BP)
