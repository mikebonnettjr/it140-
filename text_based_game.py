"""Project Two starter for the student's text-based adventure game."""

# Mike Bonnett 


def show_instructions():
    """Display the game objective and available commands."""
    # TODO: Print instructions that match your game and commands.
    print("===============================================================")
    print("              Welcome to the Temple of Akkala!")
    print(" Explore the Ancient Temple and collect all 8 items needed to")
    print("        defeat The Brood Mother and escape the Temple")
    print("\n                        Commands:")
    print("            go [direction]; (i.e. 'go north')")
    print("                get [item]; (ie. 'get Key')")
    print("             exit;   This will quit the game")
    print("===============================================================")
    pass


def show_status(current_room, player_inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
    print("-"*63)
    print(f"You are currently in {current_room}.")
    #print(f"{rooms[current_room]['description']}")
    print(f"Inventory: {player_inventory}")
    
    #room_inventory = rooms[current_room].get("item")
    #if room_inventory and room_inventory not in player_inventory:
    #    print("You see an item here: {room_inventory}")
    print("-"*63)
    pass


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.
    rooms = {
        "The Entrance to the Temple of Akkala": {"south": "The Hall of Torches"},
        
        "The Hall of Torches": {
            "north": "The Entrance to the Temple of Akkala",
            "west": "The Temple Armory",
            "south": "The Shrine of Life",
            "east": "The Blast Hollow"
            
        },
        
        "The Temple Armory": {
            "east": "The Hall of Torches", 
            "south": "The Webbed Crypt"
            
        },
        
        "The Webbed Crypt": {
            "north": "The Temple Armory"
            
        },
        
        "The Shrine of Life": {
            "north": "The Hall of Torches", 
            "south":"The Brood Mother's Lair"
            
        },
        
        "The Brood Mother's Lair": {
            "north": "The Shrine of Life"
            
        },
        
        "The Blast Hollow": {
            "west": "The Hall of Torches", 
            "south": "The Hall of Valor", 
            "east": "The Wanderer's Camp"
            
        },
        
        "The Wanderer's Camp": {
            "west": "The Blast Hollow",
            "north": "The Hidden Vault"
            
        },
        
        "The Hidden Vault": {
            "south": "The Wanderer's Camp"
            
        },
        
        "The Hall of Valor": {
            "north": "The Blast Hollow"
            
        },
     }
     
    room_inventory = {
        "The Hall of Torches": "TORCH",
        
        "The Temple Armory": "KNIGHT'S SHIELD",
        
        "The Webbed Crypt": "BOSS KEY",
        
        "The Shrine of Life": "HEART CONTAINER",
        
        "The Blast Hollow": "BOOMSHROOM",
        
        "The Wanderer's Camp": "ADVENTURER'S CLOAK",
        
        "The Hidden Vault": "SKELETON KEY",
        
        "The Hall of Valor": "THE HERO'S SWORD",
     }
     
    # TODO: Set the player's starting room.
    current_room =  "The Entrance to the Temple of Akkala"
    # TODO: Create the player's inventory.
    player_inventory = []
    # TODO: Call the instruction function at the appropriate time.
    show_instructions()
    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost
    game_over = False
    
    while not game_over:
        show_status(current_room, player_inventory, rooms)
        
        player_command = input("\nWhat will you do?\n")

        if player_command == "exit":
            print("")
            print("="*63)
            print("\n       Thanks for playing the Temple of Akkala! Goodbye!\n")
            print("="*63)
            game_over = True
    
        elif player_command.startswith("go "):

            direction = player_command.replace("go ", "")

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"\nYou explore {direction}.\n")
            
                if current_room == "The Brood Mother's Lair":
                    print("story") #fill in story and inventory requirements
                    
                    #if player_inventory = [8]:
                        #print(Story for defeating the boss)
                    game_over = True
                    #elif boss_key not in player_inventory:
                        #print("Looks like you need a key")
                    #elif player_inventory < [8]:
                        #print("You open the door and see boss. Maybe you should look around more")
                    
            else:
                print(f"\nThere are no passages to the {direction}!\n")

        elif player_command.startswith("get "):

            requested_item = player_command.replace("get ", "")

            if (
                current_room in room_inventory
                and requested_item == room_inventory[current_room].lower()
                ):
                    item_acquired = room_inventory.pop(current_room)
                    player_inventory.append(item_acquired)
                    
                    print(f"\nYou have acquired {item_acquired}!\n")
                    
            elif (requested_item in player_inventory):
                print("\nYou already have this item!\n")
                
            else:
                print("\nThat item is not here!\n")
                
        else:
            print("\nInvalid Input. Try using an accepted command.\n")
    pass


if __name__ == "__main__":
    main()
