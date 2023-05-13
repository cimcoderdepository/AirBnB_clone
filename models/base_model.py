#!/usr/bin/python3
"""A module that defines all common attributes/methods for other classes."""
from datetime import datetime
import uuid
from models.engine.__init__ import storage


class BaseModel:
    """The parent class that defines all its attributes/methods."""

    def __init__(self):
        """Initialize the BaseModel class.

        Attributes:
                    @self: # The calling self instance of class BaseModel.

                    @updated_at:
                                the current datetime when an instance is
                                created and it will be updated every time you
                                change your object.

                    @id:
                        unique uuid when an instance is created.

                    @created_at:
                                the current datetime when an instance is
                                created
        """
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of BaseModel.

        Returns:
                A human-readable, or informal, string representation of class
                BaseModel.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update and save the current datetime in updated_at attribute."""
        self.updated_at = datetime.now()
        storage.save

    def to_dict(self):
        """
        Create a dictionary representation.

        Attributes:
                    @dict_copy:
                                A copy of __dict__ that update the value of its
                                keys/values.
        Returns: dict_copy
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["created_at"] = self.created_at.isoformat()
        return dict_copy
