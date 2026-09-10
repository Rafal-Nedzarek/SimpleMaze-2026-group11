def enterNSCorridor(state):
    print("\nYou step through the interdimensional door and you are standing in a long corridor.")
    print("The floor and walls are covered in dried blood. The air is heavy and the corridor looks worn down.")

    # --- List of accessible rooms from here ---
    available_rooms = ["stairexit", "teachersroom4", "classroom2031","classroom2035"]

    # --- Command handlers ---

    def handle_look():
        """Describe the corridor and show where the player can go."""
        print("\nYou take a look around.")
        print("There are stains of blood on the wall and ground, and the corridor looks abandoned")
        print("You can see some torn off books, papers and some schools supplies on the ground")
        print("3 meters from you, lies skeleton with missing upper part of the body")
        print("You can see 4 doors to Stair Exit, Teachers Room 4, Classroom 2031 and Classroom 2035")
        print(f"- Possible doors: {', '.join(available_rooms)}")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        """List available commands and explain navigation."""
        print("\nAvailable commands:")
        print("- look around         : See what's in the corridor and where you can go.")
        print("- go <room name>      : Move to another room.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game.")
        print(f"- Possible doors: {', '.join(available_rooms)}")
        print("- Your current inventory:", state["inventory"])

    def handle_go(room_name):
        """Move to a listed room."""
        room = room_name.lower()
        if room in available_rooms:
            print(f"You walk toward the door to {room}.")
            state["previous_room"] = "corridor"
            return room
        else:
            print(f"❌ '{room_name}' is not a valid exit. Use 'look around' to see available options.")
            return None

    # --- Main corridor command loop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            room = command[3:].strip()
            result = handle_go(room)
            if result:
                return result

        elif command == "quit":
            print("👋 You leave the school and the adventure comes to an end. Game over.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")