#!/usr/bin/python3
"""This is a module that inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):  # class User inherit BaseModel
    """Class inheritance attributes.

    Attributes:
        @email:     # email attribute

        @password:  # password attribute

        @firstname: # firstname attribute

        @last_name: # last name attribute
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
