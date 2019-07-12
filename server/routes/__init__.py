"""
    This file has temporary content to get hello world working
"""
from app import app

@app.route('/')
def index():
    """
        Index route
    """
    return "Hello World!"
