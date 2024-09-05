import utils
from item import Item


class Consumable(Item):

   def __init__(self, name, info, type, amount):
      super().__init__(name, info)
      self.type = type
      self.amount = amount

   def use(self, player, index):
      print("Using " + self.name + "...")
      if self.type == "health":
         player.heal(self.amount)
         player.inv.remove(self)


def init():
   utils.consumables["red potion"] = Consumable(
       "Red Potion", "A mysterious potion which regenerates 30hp.", "health",
       30)
