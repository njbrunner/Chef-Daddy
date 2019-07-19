"""This file provides function for interacting ingredients"""
from app.models.ingredient import Ingredient
from app.utilities import response_utilities

def create_new_ingredient(ingredient_data):
    """
    Creates new ingredient.

    Parameters:
        ingredient_data: data for new ingredient

    Returns:
        status of ingredient creation
    """

    new_ingredient = Ingredient(name=ingredient_data['name'])
    new_ingredient.save()

    return new_ingredient
