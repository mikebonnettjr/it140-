"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.

rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

current_room =  "Great Hall"

game_over = False

while not game_over:
    print("You are in the " + current_room + ".\n")

    player_command = input("Which direction do you want to go?\n")

    if player_command in rooms[current_room]:
        current_room =  rooms[current_room][player_command]
        print(f"\nYou head {player_command}.\n")
    elif player_command == "exit":
        print("\nThanks for playing!\n")
        game_over = True
    else: 
        print("You cant go that way!\n")

# TODO: Run and debug all milestone cases in prototype/README.md.
