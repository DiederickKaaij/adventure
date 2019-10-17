import json

from item import Item


class Location:
    def __init__(self, name, description=None, exits=None, items=None):
        self.name = name
        self.description = description or ""
        self.exits = exits or []
        self.items = {item["name"]: Item(**item) for item in (items or [])}

    def __str__(self):
        return self.name

    def is_accessible(self, destination):
        return str(destination) in self.exits

    def describe(self):
        description = self.description
        if len(self.items) > 0:
            items = [str(item) for item in self.items]
            description += "\nEr liggen hier: %s" % ", ".join(items)
        if len(self.exits) > 0:
            exits = [str(out) for out in self.exits]
            description += "\nJe kunt naar: %s" % ", ".join(exits)
        return description