class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race (e.g., human, elf, etc.)
        self.cls = cls        # Store the player's class (e.g., warrior, mage, etc.)
        self.atk = atk        # Store the player's attack power
        self.health = health  # Store the player's health points

class Weapon:
    # TODO: create the method to intialise Weapon object attributes (same as above)
    # The Weapon should have self, name, category and damage (can shorten if needed)
    def __init__(self, name, ctgy, damage):
        self.name = name
        self.ctgy = ctgy
        self.damage = damage
# TODO: Create an 'Enemy' class.
class Enemy:
    # TODO: Create a method to initialise Enemy object attributes
    # Each enemy should have a name, race, damage and health
    def __init__(self, name, race, damage, hp):
        self.name = name
        self.race = race
        self.damage = damage
        self.hp = hp