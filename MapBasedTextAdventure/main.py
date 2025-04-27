""" -- Phase 1 --  """

#set up global variables
player = {
    'location': 'cabin', 
    'Inventory':[]
}

game_map = {
    'cabin':{'east':'yard'}, 
    'yard':{'east':'forest', 'south':'barn','west':'cabin'},
    'forest':{'west': 'yard'}, 
    'barn':{'north': 'yard'}
}

descriptions = {
    'cabin': 'You are in a quaint cabin, there is a door to the east.',
    'yard':'You find yourself in a beautiful garden. There is a forest to the east, a barn to the south, and a cabin to the west.',
    'forest':'You are in a spooky forest. The yard is back to the west.',
    'barn': 'You are in a barn. There is a locked treasure chest in the middle of the room. The'
    'yard lies to the north.'
}

items = {
    'cabin':[],
    'yard':[],
    'forest':['key'],
    'barn':[]
}

win_events = {
    'key barn': 'You unlocked the treasure chest! You win!'
}
game_over = False

""" -- Phase 3 -- """

#describe the player's current surroundings
def look(location):
    print(descriptions[location])

    # -- Phase 5 --
    if len(items[location]) > 0:
        for item in items[location]:
            print("There is a {} here.".format(item))

#update the player's location
def move(direction):
    if direction in game_map[player['location']]:
        player['location'] = game_map[player['location']][direction]
        look(player['location'])
    else: 
        print("You cannot go {}.".format(direction))

""" -- Phase 5A -- """

#describe the player's inventory
def inventory():
    if len(player["Inventory"]) > 0:
        for item in player["Inventory"]:
            print('You are carrying a {}.'.format(item))
    else: 
        print("You are not carrying anything.")

""" -- Phase 5B -- """

#pick up items and add them to the player's inventory
def get_item(item):
    if item in items[player['location']]:
        player['Inventory'].append(item)
        items[player['location']].remove(item)
        print("You picked up the {}.".format(item))
    else: 
        print("There is no {} here.".format(item))

#remove items from the players inventory
def drop_item(item):
    if item in player['Inventory']:
        # put the item to that location when we drop it
        items[player['location']].append(item)
        
        #
        player['Inventory'].remove(item)
        print("You are no longer carrying the {}.".format(item))
    else: 
        print("You can't get rid of something you don't have.")

""" -- Phase 5C -- """

#use items from the player's inventory
def use_item(item):
    global game_over
    if item in player["Inventory"]:
        if item+" "+player['location'] in win_events:
            print(win_events[item+" "+player['location']])
            game_over = True
        else: 
            print("You cannot use the {} here".format(item))
    else: 
        print("You are not carrying a {}.".format(item))

""" -- Phase 2 --  """

#handle player input until the game ends
def main():
    global game_over
    
    look(player['location'])
    while not game_over:
        choice = input("What would you like to do?\n").split(" ")
        if len(choice) < 2 or choice[0] == 'help':
            print("Please follow instruction below to proceed with the game")
            print("\nInstructions:\n")
            print("Enter 'go <'north', 'east', 'south', or 'west'>' to move.")
            print("Enter 'look' to view the room or 'inventory' to view your inventory.")
            print("Type 'get <item name>' to acquire items.")
            print("Type 'drop <item name>' to get rid of items.")
            print("Type 'use <item name>' to use items.")
            print("Type 'quit' to exit the game.\n")
        elif choice[0] == 'go':
            move(choice[1])
        elif choice[0] == 'get':
            get_item(choice[1])
        elif choice[0] == 'use':
            use_item(choice[1])
        elif choice[0] == 'drop':
            drop_item(choice[1])
        elif choice[0] == 'inventory':
            inventory()
        elif choice[0] == 'look':
            look(player['location'])
        elif choice[0] == 'quit':
            print("Goodbye.")
            game_over = True
        else:
            print("I do not understand {}.".format(choice[0]))
main()