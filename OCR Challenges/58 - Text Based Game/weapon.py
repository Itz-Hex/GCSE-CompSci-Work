import utils
from item import Item


class Weapon(Item):

   def __init__(self, name, info, damage, speed=0.2, special=None):
      super().__init__(name, info)
      self.damage = damage
      self.speed = speed
      self.special = special

   def use_special(self, *args, **kwargs):
      try:
         self.special(*args, **kwargs)
      except:
         print("This weapon doesn't have a special ability.")


def axe_spin(weapon, room):
   print("The axe spins and you feel a surge of power!")
   for enemy in room.enemies:
      enemy.damage(weapon.damage)
      if enemy.health <= 0:
         print("You killed " + enemy.name)
         room.enemies.remove(enemy)


def init():
   utils.weapons["sword"] = Weapon("Sword",
                                   "A simple sword of unknown origin.", 10)
   utils.weapons["axe"] = Weapon(
       "Axe",
       "A great lumberjack's axe, used by giants. It's sharp and deadly.",
       30,
       0.5,
       special=axe_spin)
   utils.weapons["claws"] = Weapon("Claws",
                                   "The claws of a bear, sharp and deadly.",
                                   20, 0)