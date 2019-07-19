"""This file defines the model for a recipe"""
from mongoengine import Document, fields
from app.models.ingredient import Ingredient


class RecipeStep(Document):
    """
    Defines a RecipeStep model for database

    Attributes:
        ingredients: list of ingredients for the step
        instruction: the step instruction
        notes (optional): any notes for the step
    """
    ingredients = fields.ListField(field=fields.ReferenceField(Ingredient))
    instruction = fields.StringField(required=True)
    notes = fields.StringField()


class Recipe(Document):
    """
    Defines a recipe model for database

    Attributes:
        ingredients: list of ingredients for the recipe
        name: name of the recipe
        steps: list of steps for the recipe
        summary (optional): summary of the recipe
        image (optional): image for the recipe
        notes (optional): notes for the recipe
    """
    ingredients = fields.ListField(fields.ReferenceField(Ingredient), required=True)
    name = fields.StringField(required=True)
    # steps = fields.SortedListField(field=fields.ReferenceField(RecipeStep), required=True)
    summary = fields.StringField()
    # image = fields.ImageField()
    notes = fields.StringField()

    def to_json(self, *args, **kwargs):
        # TODO: Finish overridding this to_json module
        recipe = self.to_mongo()
        return {
            "name": self.name
        }
