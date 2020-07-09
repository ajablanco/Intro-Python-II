from player import Player
from room import Room
from item import Item
import random

# Declare items

item = {
    'sword': Item('sword', 'a rusty sword said to have been blessed by Jesus himself'),

    'knife': Item('knife', 'the sharpest blade in all the land'),

    'elixir': Item('elixir', 'a special elixir to remedy any illness'),

    'food': Item('food', 'a bag full of staples such as potatoes, oats, and nuts')

}

#function to select a random item

def select_item():
    return random.choice(list(item.values()))

#declare rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [select_item()]),

    'foyer':   Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [select_item()]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [select_item()]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [select_item()]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [select_item()]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("Welcome to Aja's Adventure Game")

name = input("Please enter your name: ")

location = room['outside']

inventory = []

player = Player(name, location, inventory)

print(f"Hi {name}, {location}")

print("Choose an action")


def choose_action():
    return(input("[n] north, [s] south, [w] west, [e] east, [p] pick up item, [i] see inventory, [q] Quit\n"))

option = choose_action()

inventory_action = 0

def see_inventory():
    print('inventory: ')
    player.see_inventory()
    global option
    option = input("Choose another action: [n] north, [s] south, [w] west, [e] east, [p] pickup item, [d] drop item, [q] Quit\n")
    

def drop(item, current_room):
    for i in range(len(player.items)):
        if item == player.items[i].name:
            global room
            room[current_room].items.append(player.items[i])


def next_step():
    print(location)
    print("Choose another action...")
    global option
    option = choose_action()

def wrong_way():
    print("Oops you can't go that way, try again")
    global option
    option = choose_action()

running = True

while running:
    if option == 'q':
        print("Goodbye!")
        running = False
        break
    if location == room['outside']:
        if option == 'n':
            location = room['outside'].n_to
            next_step()
        elif option == 'p':
            pickup = input("What item do you want to pick up?")
            player.pickup_item(room['outside'].items, pickup)
            print(f'You have successfully picked up the {pickup}')
            room['outside'].remove_item(pickup)
            next_step()
        elif option == 'i':
            see_inventory()
        elif option == 'd':
            discard = input('Which item would you like to drop?')
            drop(discard, 'outside')
            player.drop_item(discard)
            print(f'You have successfully droped the {discard} at this location')
            option = choose_action()
        elif option == 'q':
            print("Goodbye!")
            running = False
            break
        else:
            wrong_way()
    elif location == room['foyer']:
        if option == 's':
            location = room['foyer'].s_to
            next_step()
        elif option == 'n':
            location = room['foyer'].n_to
            next_step()
        elif option == 'e':
            location = room['foyer'].e_to
            next_step()
        elif option == 'p':
            pickup = input("What item do you want to pick up?")
            player.pickup_item(room['foyer'].items, pickup)
            print(f'You have successfully picked up the {pickup}')
            room['foyer'].remove_item(pickup)
            next_step()
        elif option == 'i':
            see_inventory()
        elif option == 'd':
            discard = input('Which item would you like to drop?')
            drop(discard, 'foyer')
            player.drop_item(discard)
            print(f'You have successfully droped the {discard} at this location')
            option = choose_action()
        elif option == 'q':
            print("Goodbye!")
            running = False
            break
        else:
            wrong_way()

    elif location == room['overlook']:
        if option == 's':
            location = room['overlook'].s_to
            next_step()
        elif option == 'p':
            pickup = input("What item do you want to pick up?")
            player.pickup_item(room['overlook'].items, pickup)
            print(f'You have successfully picked up the {pickup}')
            room['overlook'].remove_item(pickup)
            next_step()
        elif option == 'i':
            see_inventory()
        elif option == 'd':
            discard = input('Which item would you like to drop?')
            drop(discard, 'overlook')
            player.drop_item(discard)
            print(f'You have successfully droped the {discard} at this location')
            option = choose_action()
        elif option == 'q':
            print("Goodbye!")
            running = False
            break
        else:
            wrong_way()

    elif location == room['narrow']:
        if option == 'w':
            location = room['narrow'].w_to
            next_step()
        elif option == 'n':
            location = room['narrow'].n_to
            next_step()
        elif option == 'p':
            pickup = input("What item do you want to pick up?")
            player.pickup_item(room['narrow'].items, pickup)
            print(f'You have successfully picked up the {pickup}')
            room['narrow'].remove_item(pickup)
            next_step()
        elif option == 'i':
            see_inventory()
        elif option == 'd':
            discard = input('Which item would you like to drop?')
            drop(discard, 'narrow')
            player.drop_item(discard)
            print(f'You have successfully droped the {discard} at this location')
            option = choose_action()
        elif option == 'q':
            print("Goodbye!")
            running = False
            break
        else:
            wrong_way()

    elif location == room['treasure']:
        if option == 's':
            location = room['narrow'].s_to
            next_step()
        elif option == 'p':
            pickup = input("What item do you want to pick up?")
            player.pickup_item(room['narrow'].items, pickup)
            print(f'You have successfully picked up the {pickup}')
            room['narrow'].remove_item(pickup)
            next_step()
        elif option == 'i':
            see_inventory()
        elif option == 'd':
            discard = input('Which item would you like to drop?')
            drop(discard, 'narrow')
            player.drop_item(discard)
            print(f'You have successfully droped the {discard} at this location')
            option = choose_action()
        elif option == 'q':
            print("Goodbye!")
            running = False
            break
        else:
            wrong_way()

    else:
        wrong_way()


# Write a loop that:
#
# * Prints the current room name √
# * Prints the current description (the textwrap module might be useful here).√
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game