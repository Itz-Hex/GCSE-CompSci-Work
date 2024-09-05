import utils
from copy import deepcopy


class Enemy:

   def __init__(self, name, health=20, weapon=None, speed=1.0, drop=None):
      self.name = name
      self.health = health
      self.weapon = weapon
      self.speed = speed
      self.drop = drop

   def damage(self, amount):
      self.health -= amount


def init():
   utils.enemies["goblin"] = Enemy("Goblin", 20, utils.weapons["sword"])
   utils.enemies["ogre"] = Enemy("Ogre", 30, utils.weapons["sword"], 0.8)
   utils.enemies["giant"] = Enemy("Giant", 100, utils.weapons["axe"], 1.5,
                                  deepcopy(utils.weapons["axe"]))
   utils.enemies["bear"] = Enemy("Bear", 50, utils.weapons["claws"], 0.7)
