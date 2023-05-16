#!usr/bin/python3
"""Module that inherit from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class inheriting attributes from BaseModel."""

    place_id = ""
    user_id = ""
    text = ""
