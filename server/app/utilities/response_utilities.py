"""This file provides functions for handling response messages"""
from http import HTTPStatus
from flask import make_response


def invalid_request(message):
    """
    This function creates an invalid request with provided message

    Parameters:
        message: Explains why the request was invalid

    Returns:
        response object with status and message
    """
    return make_response(
        {'Status': 'Fail',
         'Message': 'Invalid Request: {}'.format(message)
        }), HTTPStatus.BAD_REQUEST


def created_object_successfully(message, data=None):
    """
    Creates a successful creation response with provided message

    Parameters:
        message: Confirms what was created
        data (optional): any data that should be returned to the user

    Returns:
        response object with status, message, and data
    """
    return make_response(
        {'Status': 'Success',
         'Message': message,
         'Data': data
        }), HTTPStatus.CREATED


def fetched_data_successfully(message, data):
    """
    Creates a successful response with provided message and data

    Parameters:
        message: Confirms data fetch was successful
        data: data that will be returned to the user

    Returns:
        respone object with status, message, and data
    """
    return make_response(
        {'Status': 'Success',
         'Message': message,
         'Data': data
        })
