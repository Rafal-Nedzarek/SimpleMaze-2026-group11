import sys

def enterLab2001(state):
    print("Here goes the description of the room upon entering it.")

    def handle_look():
        print("You look around the room and see...")
        print("- Possible exits: corridor")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        print("\nAvailable commands:")
        print("- look around         : Examine the room and its contents.")
        # Add room-specific actions here!
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")

    def handle_take(item):
        print("Work in progress")
        # check if the key has been forged

    def handle_go(destination):
        if destination in ["corridor", "back"]:
            print("🚪 You open the door and step back into the corridor.")
            return "corridor"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    def handle_answer(answer):
        print("Work in progress")
        # check if all key shards placed on the workbench
        # check if answer is correct
        # if incorrect, replace the broken part and prompt to try again

    # --- Commandoloop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command.startswith("take "):
            item = command[5:].strip()
            handle_take(item)

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command.startswith("answer "):
            answer = command[7:].strip()
            result = handle_answer(answer)
            if result:
                return result

        elif command == "quit":
            print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")
