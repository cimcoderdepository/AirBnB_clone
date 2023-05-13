#!/usr/bin/python3
import json

class Filestorage():
    __file_path = "file.json"
    __object = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{self.__class__.__name__}.{self.id}"
        self.__object[key] = obj

    def save(self):
        with open(self.__file_path, "w",encoding="utf-8") as f:
            d = {k : v.to_dict for k, v in self.__object.items()}
            json.dump(d, f)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = eval(self.__class__.__name__(obj_dict))

        except:
            pass
            

