"""This file provides functions for handeling recipe interactions"""
from mongoengine import DoesNotExist
from app.utilities import response_utilities, ingredient_utilities
from app.models.recipe import Recipe
from app.models.ingredient import Ingredient


def create_new_recipe(recipe_data):
    """
    Creates a new recipe in the database.

    Parameters:
        recipe_data: the data needed to create a new recipe

    Returns:
        Status of recipe creation
    """
    ingredients = list()
    for ingredient in recipe_data['ingredients']:
        try:
            existing_ingredient = Ingredient.objects.get(name=ingredient['name'])
            ingredients.append(existing_ingredient)
        except DoesNotExist:
            new_ingredient = ingredient_utilities.create_new_ingredient(ingredient)
            ingredients.append(new_ingredient)

    new_recipe = Recipe(
        ingredients=ingredients,
        name=recipe_data['name']
    )
    new_recipe.save()

    return new_recipe
            


def validate_request(request, required_parameters):
    """
    Validates recipe request.

    Parameters:
        request: the forwarded http request
        required_parameters: list of parameters to validate

    Returns:
        JSON object containing boolean value associated with validity and response if failed
    """
    if not request.json:
        return {'valid': False,
                'response': response_utilities.invalid_request('Request not JSON')}

    for parameter in required_parameters:
        if parameter not in request.json:
            return {'valid': False,
                    'response': response_utilities.invalid_request(
                        '{} missing from request'.format(parameter))
                    }

    return {'valid': True}
