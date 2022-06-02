#!/usr/bin/python3
""" """


import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return __objects

    def new(self, obj):
        __object.update(obj.__class__.__name__: str(obj.id))

    def save(self):
        jstring = json.dumps(__objects)
        with open(__file_path, "w") as jfile:
            jfile.write(str(__objects))

    def reload(self):
        with open(__file_path, "r") as jfile:
            jstring = jfile.read()
            __objects = json.loads(jstring)
