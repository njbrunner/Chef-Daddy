""" File defines configuration variables"""

# System
DEBUG = False

# Database
MONGO_ADDRESS = "localhost"
MONGO_PORT = "27107"
DB_NAME = "chefDaddy"
MONGO_URI = "mongodb://{}:{}/{}".format(MONGO_ADDRESS, MONGO_PORT, DB_NAME)

# Authentication
JWT_SECRET_KEY = "enter_secret_here"