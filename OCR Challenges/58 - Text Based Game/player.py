import utils
import weapon
from room import Room
from copy import deepcopy


class Player():

   def __init__(self, name, room_name):
      self.name = name
      self.health = 100
      self.max_health = 100
      self.inv = []
      self.room = utils.world[room_name]
      self.weapon = None

   def load(self, health, max_health, inv, room, weapon, world):
      self.health = health
      self.max_health = max_health
      self.inv = []

      for item in inv:
         try:
            self.inv.append(deepcopy(utils.items[item.casefold()]))
         except:
            try:
               self.inv.append(deepcopy(utils.weapons[item.casefold()]))
            except:
               self.inv.append(deepcopy(utils.consumables[item.casefold()]))


      try:
         self.weapon = deepcopy(utils.weapons[weapon.casefold()])
      except:
         self.weapon = None

      new_world = {}
      for name, the_room in world.items():
         items = []

         for item_name in the_room[3]:
            try:
               items.append(deepcopy(utils.items[item_name.casefold()]))
            except:
               try:
                  items.append(deepcopy(utils.weapons[item_name.casefold()]))
               except:
                  items.append(deepcopy(utils.consumables[item_name.casefold()]))

         enemies = None if the_room[4] == [] else []
         if enemies is not None:
            for enemy_name in the_room[4]:
               enemies.append(deepcopy(utils.enemies[enemy_name.casefold()]))

         new_world[name] = Room(the_room[0], the_room[1], the_room[2], items,
                            enemies)

      utils.world = new_world

      self.room = utils.world[room]

   def save(self):
      inv = []

      for item in self.inv:
         inv.append(item.name)

      world = {}
      for name, room in utils.world.items():
         world[name] = [room.name, room.description, room.links, [], []]
         for item in room.items:
            world[name][3].append(item.name)

         if room.enemies:
            for enemy in room.enemies:
               world[name][4].append(enemy.name)

      return [self.health, self.max_health, inv, self.room.name, self.weapon.name if self.weapon else None, world]

   def move(self, direction):
      if direction not in self.room.links:
         print("Cannot move in this direction!")
         return
      new_room_name = self.room.links[direction]
      print("Moving to: " + new_room_name)
      self.room = utils.world[new_room_name]

   def getItem(self, new_item):
      self.inv.append(deepcopy(new_item))
      self.weapon = new_item if not self.weapon and isinstance(
          new_item, weapon.Weapon) else self.weapon

   def equip(self, index):
      if isinstance(self.inv[index], weapon.Weapon):
         self.weapon = self.inv[index]
         print("Equipped " + self.weapon.name)
      else:
         print("You cannot equip that!")

   def damage(self, amount):
      self.health -= amount

   def heal(self, amount):
      self.health += amount
      if self.health > self.max_health:
         self.health = self.max_health

   def removeItem(self, index):
      del self.inv[index]

   def checkAlive(self):
      if self.health <= 0:
         print("You died.")
         return False
      return True
