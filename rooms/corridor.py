# -----------------------------------------------------------------------------
# File: corridor.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

import sys
from functions import shared_functions as sf
from .utils import debugMode, healing

def enterCorridor(state):
    print("\nYou are standing in the school's main corridor.")
    if state["visited"]["corridor"] is False:
        print("You see a long corridor with many doors and glass walls on both side. Behind these door are rooms, waiting to be explored.")
        state["visited"]["corridor"] = True

    # --- List of accessible rooms from here ---
    available_rooms = ["lobby", "nscorridor","examroom", "enchanted_library", "teacherroom1", "projectroom3", "break_room"]

    # --- Command handlers ---

    def handle_look():
        """Describe the corridor and show where the player can go."""
        print("\nYou take a look around.")
        print("Students and teachers are walking in both directions along the corridor. You see several labeled doors.")
        print(f"- Possible doors: {', '.join(available_rooms)}")
        print("- You current inventory:", state["inventory"])

    def handle_help():
        """List available commands and explain navigation."""
        print("\nAvailable commands:")
        print("- use bandages        : Use bandages to heal 4 harts.")
        # print("- look around         : See what's in the corridor and where you can go.")
        # print("- go <room name>      : Move to another room. Example: go enchanted_library")
        # print("- ?                   : Show this help message.")
        # print("- quit                : Quit the game.")
        sf.show_universal_help_text()

    def handle_go(room_name):
        """Move to a listed room."""
        room = room_name.lower()
        if room in available_rooms:
            print(f"You walk toward the door to {room}.")
            state["previous_room"] = "corridor"
            return room
        else:
            print(f"'{room_name}' is not a valid exit. Use 'look around' to see available options.")
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

            if room == "lobby" and state["section_finished"]["medieval"] is False and state["section_finished"]["chinese"] is False:
                print("You can't enter the door is locked")
            elif room == "nscorridor" and state["section_finished"]["scifi"] is False:
                print("You can't enter the door is locked")
            else:
                result = handle_go(room)
                if result:
                    return result
        elif command == "use bandages":
            if "bandages" in state["inventory"]:
                healing(state)
            else:
                print("You don't have any bandages.")

        elif command == "quit":
            print("You leave the school and the adventure comes to an end. Game over.")
            sys.exit()

        # not shown to the player
        elif command.startswith("debug add "):
            state["inventory"] += debugMode(command)

        elif command == "status":
            sf.show_completion(state["completed"])

        else:
            print("Unknown command. Type '?' to see available commands.")
