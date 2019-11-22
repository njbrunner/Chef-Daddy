"""
    This file is used to run the application in a development setting
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
