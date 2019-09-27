"""This file contains all the endpoints to handle user authentication"""
from flask import Blueprint, request
from app.utilities import auth_utilities, response_utilities

AUTH_BP = Blueprint('auth_bp', __name__, url_prefix='/auth')


@AUTH_BP.route('/register', methods=["POST"])
def register():
    """Handles registering a new user

    Parameters:
        http request

    Returns:
        response object with status of user registration
    """
    user_data = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    return auth_utilities.register_user(user_data)


@AUTH_BP.route('/login', methods=["POST"])
def login():
    """Handles logging in a new user

    Parameters:
        http request

    Returns:
        response object with status of user login and authentication token if successful
    """
    user_data = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    return auth_utilities.login_user(user_data)
