"""This file provides functions to assist user authentication."""
from werkzeug.security import generate_password_hash
from mongoengine import DoesNotExist, ValidationError
from flask_jwt_extended import create_access_token
from app.utilities import response_utilities
from app.models.user import User

def register_user(user_data):
    """Registers a new user in the database.

    Parameters:
        user_data: JSON containing user email and password

    Returns:
        Message containing status of registration
    """
    try:
        user = User(
            email=user_data['email'],
            hashed_password=generate_password_hash(user_data['password'])
        )
        user.save()
        return response_utilities.created_object_successfully(
            f'Registered new user: {user.email}'
        )

    except ValidationError:
        return response_utilities.invalid_request("Could not register user")


def login_user(user_data):
    """Returns an authenticated token if email and hashed password match a user in the database.

    Parameters:
        user_data: JSON containing user email and password

    Returns:
        response object with valid authentication token to verify user is logged in
    """
    user = User.objects(email=user_data['email']).first()
    if user.check_user_provided_password(user_data['password']):
        return response_utilities.authenticated_user_successfully(
            user_email=user.email,
            token=create_access_token(identity=user.email)
        )

    return response_utilities.invalid_request('Could not authenticate user')


# def validate_request(request, required_parameters):
#     """
#     Validates request contains proper format and parameters.

#     Parameters:
#         request: the forwarded http request
#         required_parameters: list of parameters to validate

#     Returns:
#         JSON object containing boolean value associated with validity and response if failed
#     """

#     if not request.json:
#         return {'valid': False, 'message': 'Request not JSON'}

#     for parameter in required_parameters:
#         if parameter not in request.json:
#             return {'valid': False, 'message': '{} missing from request'.format(parameter)}

#     return {'valid': True}
