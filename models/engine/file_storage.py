#!/usr/bin/python3
"""Serialize instances to JSON file and deserialize JSON file to instances."""
import json
from models.base_model import BaseModel
<<<<<<< HEAD
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
=======


class FileStorage:
    """Initialize a class FileStorage.

    Attributes:
                @__file_path:   # a JSON file to log every instances per call.

                @__objects:     # an empty dictionary but will store all
                                # objects each time an instance is called
    """
>>>>>>> b5101eb8f0bee183c393165de876b39dc29e4328

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Instance method that return the dictionary."""
        return self.__objects

    def new(self, obj):
        """Set empty dictionary to populate the values to keys.

        key:    # dictionary key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize dictionary to the JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserialize the JSON file to dictionary."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
<<<<<<< HEAD
                    cls_name =o["__class__"]
                    del o["__class__"]
                    self.new(eval(f"{cls_name}")(**o))

        except FileNotFoundError:
            return
            
=======
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(f"base_model.{cls_name}")(**o))
>>>>>>> b5101eb8f0bee183c393165de876b39dc29e4328

        except FileNotFoundError:
            return
