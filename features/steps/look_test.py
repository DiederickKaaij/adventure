from behave import given, when, then #pylint: disable=no-name-in-module
from game import Game

@given(u'a player is in hal')
def test_move_hal(context):
    context.game = Game.load("data/test_game.json")
    context.game.move("hal")

@when(u'they type bekijk hal')
def test_bekijk(context):
    context.description = context.game.describe("hal")

@then(u'they should get a description of hal')
def test_description(context):
    assert context.description == "een ruimte die andere ruimtes met elkaar vebindt"