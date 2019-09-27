"""This file provides functions for handeling recipe interactions"""
from mongoengine import DoesNotExist
from flask import current_app
from app.utilities import response_utilities
from app.models.recipe import Recipe


def create_new_recipe(recipe_data):
    """Creates a new recipe in the database.

    Parameters:
        recipe_data: the data needed to create a new recipe

    Returns:
        Response object with status of recipe creation
    """
    try:
        new_recipe = Recipe(
            ingredients=recipe_data['ingredients'],
            description=recipe_data['description'],
            name=recipe_data['name']
        )
        new_recipe.save()
        return response_utilities.created_object_successfully('recipe', data=new_recipe.to_mongo())

    except Exception:
        return response_utilities.invalid_request('unable to create recipe')


def get_recipies():
    """Retrieves recipe data from the database

    Returns:
        Response object with recipe data
    """
    try:
        recipies = Recipe.objects
        recipe_dicts = list()
        for recipe in recipies:
            recipe_dict = recipe.to_mongo()
            recipe_dict['_id'] = str(recipe_dict['_id'])
            recipe_dicts.append(recipe_dict)
        current_app.logger.info(recipe_dicts)

        return response_utilities.fetched_data_successfully('recipies', recipe_dicts)

    except Exception:
        return response_utilities.invalid_request('unable to fetch recipies')


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
