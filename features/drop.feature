Feature: Dropping an inventory item

    Scenario:
        Given a player has a boek
        When they type leg boek
        Then they should no longer have the boek
        And the boek should be in the current location