import json


class Item:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description or ""

    def __str__(self):
        return self.name

    def describe(self):
        return self.description