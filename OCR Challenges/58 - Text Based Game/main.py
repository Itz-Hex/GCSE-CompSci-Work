# See game instructions & map here: https://docs.google.com/spreadsheets/d/1qBXGT131ndtmYP4FDqvO6RmPwHxLwbCRgGYAcE7KCRM/edit?gid=0#gid=0

import utils
from player import Player
import room
import item
import weapon
import enemy
import consumable

from inputimeout import inputimeout
from getpass import getpass
from ast import literal_eval
import bcrypt

def look(player):
    print(player.room.description)
    if player.room.enemies:
        print("Enemies in this room:")
        for enemy in player.room.enemies:
            print("- " + enemy.name + " (" + str(enemy.health) + " health)")
    if player.room.items:
        print("Items in room:")
        for item in player.room.items:
            print("- " + item.name)
    print("Exits:")
    for link in player.room.links:
        print("- " + link + ": " + player.room.links[link].title())


def get(command, player):
    list_name = command.split(" ")[1:]
    item_name = ""
    for x in list_name:
        item_name += x + " "
    item_name = item_name[:-1]
    for item in player.room.items:
        if item.name == item_name:
            player.getItem(item)
            print("You got a " + item.name + "!")
            player.room.items.remove(item)
            break
    else:
        print("Item not found!")


def attack(command, player):
    enemy_name = command.split(" ")[1]
    for e in player.room.enemies:
        if e.name == enemy_name:
            e.damage(player.weapon.damage)
            print("You attacked the " + e.name + " and dealt " +
                  str(player.weapon.damage) + " damage!")

            if e.health <= 0:
                print("You killed " + e.name)
                if e.drop:
                    player.room.add_item(e.drop)
                    print("The " + e.name + " dropped a " + e.drop.name + "!")
                player.room.enemies.remove(e)
            else:
                try:
                    command = inputimeout(prompt='>>',
                                          timeout=(e.speed -
                                                   player.weapon.speed))
                    if command == "dodge":
                        print("You dodged the " + e.name + "'s attack!")
                    else:
                        player.damage(e.weapon.damage)
                        print("You took " + str(e.weapon.damage) +
                              " damage from the " + e.name + "'s attack!")
                except:
                    player.damage(e.weapon.damage)
                    print("You took " + str(e.weapon.damage) +
                          " damage from the " + e.name + "'s attack!")
            break
    else:
        print("Enemy not found!")


def status(player):
    print("Health: " + str(player.health))
    print("Weapon: " + str(player.weapon.name if player.weapon else "None"))
    print("Damage: " + str(player.weapon.damage if player.weapon else 0))


def inv(player):
    for i, _item in enumerate(player.inv):
        print(str(i) + ": " + _item.name)

def login():
    while True:
        name = input("Enter your name: ")
        password = getpass("Enter your password: ")

        hash_pass = ""
        f = open("users.csv", "r")
        for line in f:
            if name == line.split(",")[0]:
                hash_pass = line.split(",")[1].split("\n")[0].encode('utf-8')

        if hash_pass == "":
            print("Invalid username or password, try again.")
            continue
        
        if bcrypt.checkpw(password.encode('utf-8'), hash_pass):
            return Player(name, utils.start)
        else:
            print("Invalid username or password, try again.")

def signup():
    name = input("Enter your name: ")
    password = getpass("Enter a password: ")
    confirm_password = getpass("Confirm your password: ")
    
    while password != confirm_password:
        print("Passwords do not match, please try again.")
        password = getpass("Enter your password: ")
        confirm_password = getpass("Confirm your password: ")

    encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    f = open("users.csv", "a")
    f.write(name + "," + encrypted_password.decode("utf-8") + ",[]\n")
    f.close()

    print("Account created successfully!")
    return Player(name, utils.start)

def load(player):
    file = open("users.csv", "r")
    for line in file:
        if line.split(",")[0] == player.name:
            data = ""
            for i in line.split(",")[2:]:
                data += i + ","
            data = data[:-1]
            if "," not in data:
                return
            player.load(*literal_eval(data))

def quit(player):
    save_data = player.save()
    f = open("users.csv", "r")
    data = f.readlines()
    f.close()
    for i, line in enumerate(data):
        if line.split(",")[0] == player.name:
            data[i] = player.name + "," + line.split(",")[1] + "," + str(save_data) + "\n"
            break
    f = open("users.csv", "w")
    f.writelines(data)
    f.close()

def main():
    player = None
    choice = input("Login/Signup? (l/s) ")
    if choice == "l":
        player = login()
    elif choice == "s":
        player = signup()
    else:
        print("Invalid choice!")
        main()

    load(player)
    
    while True:
        if not player.checkAlive():
            quit(player)
            break

        command = input('>>')
        if command in {'N', 'E', 'S', 'W'}:
            player.move(command)
        elif "look" in command:
            look(player)
        elif "get" in command:
            get(command, player)
        elif "attack" in command:
            attack(command, player)
        elif "status" in command:
            status(player)
        elif "inv" in command:
            inv(player)
        elif "equip" in command:
            try:
                player.equip(int(command.split(" ")[1]))
            except:
                print("Invalid index!")
        elif "use" in command:
            try:
                index = int(command.split(" ")[1])
                player.inv[index].use(player, index)
            except:
                print("You cannot use that!")
        elif "special" in command:
            player.weapon.use_special(player.weapon, player.room)
        elif "quit" in command:
            quit(player)
            
            break
        else:
            print('Invalid command')


if __name__ == "__main__":
    utils.init()
    item.init()
    weapon.init()
    enemy.init()
    consumable.init()
    room.init()
    main()
