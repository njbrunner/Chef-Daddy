"""This file defines the model for an ingredient"""
from mongoengine import Document, fields

class Ingredient(Document):
    """
    Defines an ingredient model for the database

    Attributes:
        name: name of the ingredient
        quantity: how much/many of the ingredient
    """
    name = fields.StringField(required=True)
    #quantity = fields.StringField(required=True)
