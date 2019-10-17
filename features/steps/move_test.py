from behave import given, when, then #pylint: disable=no-name-in-module
from game import Game

@given(u'a player is in keuken')
def test_start(context):
    context.game = Game.load("data/test_game.json")

@when(u'they type ga hal')
def test_commando(context):
    context.game.move("hal")

@then(u'the new location should be hal')
def test_new_location(context):
    assert str(context.game.location) == "hal"