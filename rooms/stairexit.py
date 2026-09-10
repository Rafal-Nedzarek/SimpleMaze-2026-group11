# -----------------------------------------------------------------------------
# File: stairexit.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

import sys
from .utils import chooseNextRoom

def enterStairExit(state):
    print("\nYou push the door to the stair exit and you enter the room.")
    print("The stairwell has collapsed, concrete and twisted railing block the way completely.")

    # --- Command handlers ---

    def handle_look():
        """Describe the lobby and show exits."""
        print("\nYou take a slow look around.")
        print("Chunks or rubble is piled where the stairs used to be")
        print("To your left is a wooden chest")
        print("- Possible exit: NSCorridor")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        """Show help message with available commands."""
        print("\nAvailable commands:")
        print("- open chest          : See what’s in the chest.")
        print("- look around         : See what’s in the lobby.")
        print("- go nscorridor / back  : Return to the main corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game.")

    def handle_go(destination):
        """Handle movement to another room."""
        if destination in ["nscorridor", "back"]:
            print("You leave the stair exit and head back into the nscorridor.")
            state["previous_room"] = "stairexit"
            return "nscorridor"
        else:
            print(f"You can't go to '{destination}' from here.")
            return None

    # --- Main command loop ---
    opened_chest = False
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "open chest" and opened_chest == False:
            print("\nYou open the chest and you have received bandages")
            print("When you use bandages you will gain 4 hearts")
            state["inventory"].append("bandages")
            print("- Your current inventory:", state["inventory"])
            opened_chest = True

        elif command == "open chest" and opened_chest == True:
            print("\nYou have already opened this chest")

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("👋 You suddenly explode. Game over.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")
