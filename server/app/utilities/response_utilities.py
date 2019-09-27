"""This file provides functions for handling response messages"""
from http import HTTPStatus
from flask import make_response


def invalid_request(message):
    """Creates an invalid request with provided message

    Parameters:
        message: Explains why the request was invalid

    Returns:
        response object with status and message
    """
    return make_response({
        'Status': 'Fail',
        'Message': f'Invalid Request: {message}'
    }), HTTPStatus.BAD_REQUEST


def created_object_successfully(object_type, data=None):
    """Creates a successful creation response with provided message

    Parameters:
        object_type: the object type that was created
        data (optional): any data that should be returned to the user

    Returns:
        response object with status, message, and data
    """
    return make_response({
        'Status': 'Success',
        'Message': f'Successfully created {object_type}',
        'Data': data
    }), HTTPStatus.CREATED


def fetched_data_successfully(object_type, data):
    """Creates a successful response with provided message and data

    Parameters:
        object_type: the object type that was fetched
        data: data that will be returned to the user

    Returns:
        respone object with status, message, and data
    """
    return make_response({
        'Status': 'Success',
        'Message': f'Successfully fetched {object_type}',
        'Data': data
    })


def authenticated_user_successfully(user_email, token):
    """Creates a successful respone with authentication token

    Parameters:
        user_email: email of the user that was authenticated
        token: authentication token to be returned to the client

    Returns:
        response object with status, message, and token
    """
    return make_response({
        'Status': 'Success',
        'Message': f'Successfully authenticated user: {user_email}',
        'Data': {'chef_token': token}
    })
