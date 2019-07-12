"""
    Creates the application
"""
from flask import Flask

# CREATE app
app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile(filename='..\\instance\\config.py')

import routes
