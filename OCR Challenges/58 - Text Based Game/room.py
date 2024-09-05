import utils
from copy import deepcopy


class Room():

    def __init__(self, name, description, links, items=[], enemies=None):
        self.name = name
        self.description = description
        self.links = links
        self.items = items 
        self.enemies = enemies

    def add_item(self, item):
        self.items.append(item)


def init():
    utils.world['forest'] = Room(
        "forest", "You are in a forest. To the north, you can see a clearing.",
        {'N': 'a clearing'})

    utils.world['a clearing'] = Room(
        'a clearing',
        "You come to a clearing, and in its centre is a sword on a pedestal.",
        {
            'N': 'clearing north',
            'S': 'forest',
            'E': 'clearing east',
            'W': 'clearing west'
        },
        items=[
            deepcopy(utils.weapons["sword"]),
            deepcopy(utils.consumables["red potion"])
        ])

    utils.world['clearing north'] = Room(
        'clearing north',
        "You move to the northern part of the clearing, beyond a hedge. An ogre and two goblins jump toward you.",
        {
            'S': 'a clearing',
            'E': 'forest east',
            'W': 'forest west'
        },
        enemies=[
            deepcopy(utils.enemies["goblin"]),
            deepcopy(utils.enemies["goblin"]),
            deepcopy(utils.enemies["ogre"])
        ])

    utils.world['clearing east'] = Room(
        'clearing east',
        "You move to the eastern part of the clearing, past a decrepit stone brick wall. There is a hut in the centre of the clearing, and a goblin is sticking its head out of the window. It calls its friends out of the goblin hut and they begin to charge toward you.",
        {
            'N': 'forest east',
            'W': 'a clearing'
        },
        enemies=[
            deepcopy(utils.enemies["goblin"]),
            deepcopy(utils.enemies["goblin"]),
            deepcopy(utils.enemies["goblin"]),
            deepcopy(utils.enemies["goblin"]),
            deepcopy(utils.enemies["goblin"])
        ])

    utils.world['clearing west'] = Room(
        'clearing west',
        "You move to the western part of the clearing, through some shrubs. As you walk further into the clearing, you hear a goblin approaching from behind.",
        {
            'N': 'forest west',
            'E': 'a clearing'
        },
        enemies=[deepcopy(utils.enemies["goblin"])])

    utils.world['forest east'] = Room(
        'forest east',
        "You exit the clearing, back into the forest. Within the darkness, you can see a giant stomping toward you.",
        {
            'S': 'clearing east',
            'W': 'clearing north'
        },
        enemies=[deepcopy(utils.enemies["giant"])])

    utils.world['forest west'] = Room(
        'forest west',
        "You exit the clearing, back into the forest. Beyond a tree, you can see a bear scratching its claws down it. It roars as it hears you and begins to charge toward you.",
        {
            'S': 'clearing west',
            'E': 'clearing north'
        },
        enemies=[deepcopy(utils.enemies["bear"])])
