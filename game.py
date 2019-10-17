import json

from location import Location
from item import Item
from player import Player


class Game:
    def __init__(self, name, location=None, target=None, locations=None, items=None):
        self.name = name
        self.locations = {
            location["name"]: Location(**location) for location in (locations or [])
        }
        
        location = self.find_location(
            location, locations[0]["name"] if locations else None
        )
        items = {item["name"]: Item(**item) for item in (items or [])}
        self.player = Player("speler", location, items)

        self.target = self.find_location(
            target, locations[-1]["name"] if locations else None
        )

    def __str__(self):
        return self.name

    @classmethod
    def load(cls, filename):
        print('Loading game "%s"' % filename)
        with open(filename) as fin:
            data = json.load(fin)
        return Game(**data)

    def find_location(self, location, default=None):
        if len(self.locations) > 0:
            if location in self.locations:
                return self.locations[location]
            elif default in self.locations:
                return self.locations[default]
        return None

    def is_done(self):
        return self.player.location == self.target

    def move(self, destination):
        destination = self.find_location(destination)
        self.player.move(destination)

    def get(self, item):
        self.player.get(item)

    def drop(self, item):
        self.player.drop(item)

    def get_location(self):
        return self.player.location

    def describe(self, key):
        key = str(key)
        return self.player.describe(key) or 'Een "%s" kan je hier niet zien.' % key
