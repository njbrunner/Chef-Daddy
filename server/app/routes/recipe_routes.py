"""This file contains endpoints to handle recipe interactions."""
import sys
from flask import Blueprint, request, current_app
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
        recipe data
    """
    return recipe_utilities.get_recipies()


@RECIPE_BP.route('/', methods=["POST"])
# @jwt_required
def create_new_recipe():
    """Handles new recipe creation.

    Parameters:
        http request

    Returns:
        status of recipe creation
    """

    recipe_data = {
        'name': request.json.get('name'),
        'description': request.json.get('description'),
        'ingredients': request.json.get('ingredients')
    }
    return recipe_utilities.create_new_recipe(recipe_data)
