# Simple text adventure engine

Run with `python shell.py <game.json>`.

Game files are in the `data` folder. 
For example: `python shell.py data/test_game.json`.

## Features

What can this engine do:

* it can load a game from a json file
* inside a game the user can move between locations (if they are connected)
* inside a game the user can pick up objects (if it is at the current location)
* inside a game the user can drop objects (if it is in possession) in a location
* inside a game the user can ask for descriptions

The objective of the game is to get to a target location.
