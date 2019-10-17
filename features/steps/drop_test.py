from behave import given, when, then #pylint: disable=no-name-in-module
from game import Game

@given(u'a player has a boek')
def test_inventory(context):
    context.game = Game.load("data/test_game.json")
    assert "boek" in context.game.items

@when(u'they type leg boek')
def test_drop(context):
    context.game.drop("boek")

@then(u'they should no longer have the boek')
def test_empty(context):
    assert "boek" not in context.game.items

@then(u'the boek should be in the current location')
def test_grond(context):
    assert "boek" in context.game.location.items