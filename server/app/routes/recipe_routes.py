"""This file contains endpoints to handle recipe interactions."""
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.utilities import recipe_utilities, response_utilities

RECIPE_BP = Blueprint('recipe_bp', __name__, url_prefix='/recipe')


@RECIPE_BP.route('/', methods=["GET"])
# @jwt_required
def get_recipies():
    """Handles returning recipe information

    Parameters:
        http request

    Returns:
        Response object with list of recipies
    """
    try:
        recipies = recipe_utilities.get_recipies()
        return response_utilities.fetched_data_successfully("recipies", recipies)
    except Exception as e:
        return response_utilities.invalid_request('unable to fetch recipies')


@RECIPE_BP.route('/', methods=["POST"])
# @jwt_required
def create_new_recipe():
    """Handles new recipe creation.

    Parameters:
        http request

    Returns:
        Response object with created recipe
    """
    try:
        recipe = recipe_utilities.create_new_recipe(request.json)
        return response_utilities.created_object_successfully("recipe", recipe)
    except Exception as e:
        return response_utilities.invalid_request('unable to create recipe')