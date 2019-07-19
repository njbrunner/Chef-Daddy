"""
    This file is used to run the application in a development setting
"""
from app import APP

if __name__ == "__main__":
    APP.run(debug=APP.config["DEBUG"], port=80)
