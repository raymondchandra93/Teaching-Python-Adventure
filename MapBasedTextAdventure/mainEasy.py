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
    'barn': 'You are in a barn. There is a treasure chest in the middle of the room. The'
    'yard lies to the north.'
}

game_over = False
treasure_acquired = False

""" -- Phase 3 -- """

#describe the player's current surroundings
def look(location):
    print(descriptions[location])

#update the player's location
def move(direction):
    global game_over, treasure_acquired


    if direction in game_map[player['location']]:
        player['location'] = game_map[player['location']][direction]
        
        # Win if the treasure has been acquired
        if player['location'] == 'cabin' and treasure_acquired:
            print("You returned the treasure safely. You win!")
            game_over = True
            return
        
        look(player['location'])
        
        if player['location'] == 'barn' and not treasure_acquired:
            print("You open the chest and collect the treasure. You should get the treasure back to the cabin!")
            treasure_acquired = True
    else: 
        print("You cannot go {}.".format(direction))

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
            print("Type 'quit' to exit the game.\n")
        elif choice[0] == 'go':
            move(choice[1])
        elif choice[0] == 'look':
            look(player['location'])
        elif choice[0] == 'quit':
            print("Goodbye.")
            game_over = True
        else:
            print("I do not understand {}.".format(choice[0]))
main()