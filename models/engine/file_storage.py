#!/usr/bin/python3
""" """


import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = obj.to_dict().copy()
        self.__objects.update({obj.__class__.__name__: str(obj.id)})

    def save(self):
        jstring = json.dumps(self.__objects)
        with open(self.__file_path, "w") as jfile:
            jfile.write(str(self.__objects))

    def reload(self):
        try:
            with open(self.__file_path, "r") as jfile:
                jstring = jfile.read()
                __objects = json.loads(jstring)
        except:
            pass
