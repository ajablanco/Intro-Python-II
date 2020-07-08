from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

player = Player(name, location)

print(f"Hi {name}, {location}")

print("Where do you want to go next?")


def choose_direction():
    return(input("[n] north, [s] south, [w] west, [e] east, [9] Quit\n"))


option = choose_direction()

def next_step():
    print(location)
    print("Where do you want to go next?")
    global option
    option = choose_direction()

def wrong_way():
    print("Oops you can't go that way, try again")
    global option
    option = choose_direction()

while not option == 9:
    if location == room['outside']:
        if option == 'n':
            location = room['outside'].n_to
            next_step()
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
        else:
            wrong_way()
    elif location == room['overlook']:
        if option == 's':
            location = room['overlook'].s_to
            next_step()
        else:
            wrong_way()
    elif location == room['narrow']:
        if option == 'w':
            location = room['narrow'].w_to
            next_step()
        elif option == 'n':
            location = room['narrow'].n_to
            next_step()
        else:
            wrong_way()
    elif location == room['treasure']:
        if option == 's':
            location = room['narrow'].s_to
            next_step()
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