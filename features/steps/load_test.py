from behave import given, when, then #pylint: disable=no-name-in-module
from game import Game

@given(u'we load in the gamefile')
def test_loading(context):
    context.game = Game.load("data/test_game.json")

@when(u'we check our location')
def test_location(context):
    context.location = context.game.location

@then(u'it should be the keuken')
def test_keuken(context):
    assert str(context.location) == "keuken"