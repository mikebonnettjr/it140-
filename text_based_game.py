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


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
    print("--------------------------------------------")
    print(f"You are currenly in {current_room}.")
    #print(f"{rooms[current_room]['description']}")
    print(f"Inventory: {player_inventory}")
    
    room_inventory = rooms[current_room].get("item")
    if room_inventory and room_inventory not in player_inventory:
        print("You see an item here: {room_inventory}")
    print("--------------------------------------------")
    pass


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.
    rooms = {
        "The Entrance to the Temple of Akkala": {"south": "The Hall of Torches"},
        "The Hall of Torches": {"north": "The Entrance to the Temple of Akkala", "west": "The Temple Armory", "south": "The Shrine of Life", "east": "The Blast Hollow"},
        "The Temple Armory": {"east": "The Hall of Torches", "south": "The Webbed Crypt"},
        "The Webbed Crypt": {"north": "The Temple Armory"},
        "The Shrine of Life" : {"north": "The Hall of Torches", "south": "The Brood Mother's Lair"},
        "The Brood Mother's Lair": {"north": "The Shrine of Life"},
        "The Blast Hollow": {"west": "The Hall of Torches", "south": "The Hall of Valor", "east": "The Wanderer's Camp"},
        "The Wanderer's Camp": {"west": "The Blast Hollow", "north": "The Hidden Vault"},
        "The Hidden Vault": {"south": "The Wanderer's Camp"},
        "The Hall of Valor": {"north": "The Blast Hollow"},
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
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
