"""This file contains endpoints to handle recipe interactions."""
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.utilities import recipe_utilities, response_utilities

RECIPE_BP = Blueprint('recipe_bp', __name__, url_prefix='/recipe')


@RECIPE_BP.route('/new', methods=["POST"])
@jwt_required
def create_new_recipe():
    """
    Handles new recipe creation.

    Parameters:
        http request

    Returns:
        status of recipe creation
    """

    valid_response = recipe_utilities.validate_request(request, ['ingredients', 'name', 'steps'])

    if not valid_response['valid']:
        return valid_response['response']

    recipe = recipe_utilities.create_new_recipe(request.json)
    return response_utilities.created_object_successfully(
        message='Created new recipe: {}'.format(recipe.name),
        data=recipe.to_mongo()
    )
