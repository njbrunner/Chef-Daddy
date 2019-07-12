"""
    This file is used to run the application in a development setting
"""
from app import app

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], port=80)
