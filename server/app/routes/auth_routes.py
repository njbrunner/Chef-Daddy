"""This file contains all the endpoints to handle user authentication"""
from flask import Blueprint, request
from app.utilities import auth_utilities, response_utilities

AUTH_BP = Blueprint('auth_bp', __name__, url_prefix='/auth')


@AUTH_BP.route('/register', methods=["POST"])
def register():
    """
    Handles registering a new user

    Parameters:
        http request

    Returns:
        status of user registration
    """

    valid_response = auth_utilities.validate_request(request, ['email', 'password'])

    if not valid_response['valid']:
        return valid_response['response']

    return auth_utilities.register_user(request.json)


@AUTH_BP.route('/login', methods=["POST"])
def login():
    """
    Handles logging in a new user

    Parameters:
        http request

    Returns:
        Status of user login and authentication token if successful
    """

    valid_response = auth_utilities.validate_request(request, ['email', 'password'])

    if not valid_response['valid']:
        return valid_response['response']

    return auth_utilities.login_user(request.json)
