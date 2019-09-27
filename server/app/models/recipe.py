"""This file defines the model for a recipe"""
from mongoengine import Document, fields


class Recipe(Document):
    """Defines a recipe model for database

    Attributes:
        ingredients: list of ingredients for the recipe
        name: name of the recipe
        steps: list of steps for the recipe
        description (optional): description of the recipe
        image (optional): image for the recipe
        notes (optional): notes for the recipe
        cook_time (optional): time to cook the recipe
        prep_time (optional): time to prep ingredients for the recipe
    """
    # ingredients = fields.ListField(fields.ReferenceField(Ingredient), required=True)
    ingredients = fields.ListField(fields.DictField(), required=True)
    # ingredients = fields.ListField(fields.EmbeddedDocumentField(Ingredient), required=True)
    name = fields.StringField(required=True)
    # steps = fields.SortedListField(field=fields.ReferenceField(RecipeStep), required=True)
    description = fields.StringField()
    # image = fields.ImageField()
    # notes = fields.StringField()
    # cook_time = fields.StringField()

    def validate_recipe_data(recipe_data) -> bool:
        """Checks the validity of the provided recipe data
        
        Parameters:
            recipe_data: user defined data for a new recipe

        Returns:
            returns true if valid recipe data otherwise false
        """
        required_parameters = ['name', 'ingredients']
        for parameter in required_parameters:
            if parameter not in recipe_data:
                return False
        return True
