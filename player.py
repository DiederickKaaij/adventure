import json

from location import Location
from item import Item


class Player:
    def __init__(self, name, location, items=None):
        self.name = name
        self.location = location
        self.items = items or []

    def __str__(self):
        return self.name

    def move(self, destination):
        if not (destination and self.location.is_accessible(destination)):
            raise KeyError(
                "%s is vanuit %s niet te bereiken" % (destination, self.location)
            )
        elif destination == self.location:
            raise KeyError("Daar ben je al.")
        self.location = destination

    def get(self, item):
        try:
            item = self.location.items.pop(item)
            self.items[str(item)] = item
        except KeyError:
            raise KeyError("Er is geen %s in %s" % (item, self.location))

    def drop(self, item):
        try:
            item = self.items.pop(item)
            self.location.items[item.name] = item
        except KeyError:
            raise KeyError("Je hebt geen %s" % item)

    def describe(self, key):
        obj = None
        if key == str(self.location):
            obj = self.location
        elif key in self.items:
            obj = self.items[key]
        elif key in self.location.items:
            obj = self.location.items[key]

        if obj:
            return obj.describe()
        elif key == "spullen":
            items = [str(item) for item in self.items]
            return ", ".join(items)

        return None
