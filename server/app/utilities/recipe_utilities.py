"""This file provides functions for handeling recipe interactions"""
from mongoengine import DoesNotExist
from flask import current_app
from app.utilities import response_utilities
from app.models.recipe import Recipe


def create_new_recipe(recipe_data: dict) -> dict:
    """Creates a new recipe in the database.

    Parameters:
        recipe_data: the data needed to create a new recipe

    Returns:
        Dictionary corresponding to created recipe
    """
    new_recipe = Recipe(
        ingredients=recipe_data['ingredients'],
        description=recipe_data['description'],
        name=recipe_data['name']
    )
    new_recipe.save()
    return new_recipe.to_json()


def get_recipies() -> list:
    """Retrieves recipe data from the database

    Returns:
        List of dictionaries for all the recipies
    """
    recipies = Recipe.objects
    recipe_dicts = list()
    for recipe in recipies:
        recipe_dict = recipe.to_mongo()
        recipe_dict['_id'] = str(recipe_dict['_id'])
        recipe_dicts.append(recipe_dict)
    current_app.logger.info(recipe_dicts)

    return recipe_dicts


# def validate_request(data, required_parameters):
#     """
#     Validates recipe request.

#     Parameters:
#         request: the forwarded http request
#         required_parameters: list of parameters to validate

#     Returns:
#         JSON object containing boolean value associated with validity and response if failed
#     """
#     for parameter in required_parameters:
#         if parameter not in data:
#             return {'valid': False,
#                     'response': response_utilities.invalid_request(
#                         f'{parameter} missing from request'
#                     )}

#     return {'valid': True}
