"""This file defines the model for a user"""
from datetime import datetime
from werkzeug.security import check_password_hash
from mongoengine import fields, Document

class User(Document):
    """
    Defines a user model for the database

    Attributes:
        email: The unique email used to register the user
        hashed_password: The string representation of the user's hashed password
        date_registered: The date the user registered for an account
        email_verified: A flag to track whether the user has verified their email
    """
    email = fields.EmailField(unique=True, required=True)
    hashed_password = fields.StringField(required=True)
    date_registered = fields.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    email_verified = fields.BooleanField(default=False)


    def validate_password(self, user_provided_password):
        """
        Checks the validity of the user provided password

        Parameters:
            user_provided_password: password entered by the user

        Returns:
            Boolean value associated with validity of user provided password
        """
        return check_password_hash(self.hashed_password, user_provided_password)
