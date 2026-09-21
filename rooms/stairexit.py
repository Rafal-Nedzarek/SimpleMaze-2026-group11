# -----------------------------------------------------------------------------
# File: stairexit.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

import sys
from .utils import chooseNextRoom

def enterStairExit(state):
    print("\nYou push the door to the stair exit and you enter the room.")
    if state["visited"]["stairexit"] is not True:
        print("The stairwell has collapsed, concrete and twisted railing block the way completely.")
    state["visited"]["stairexit"] = True

    # --- Command handlers ---

    def handle_look():
        """Describe the room and show exits."""
        print("\nYou take a slow look around.")
        print("Chunks or rubble is piled where the stairs used to be")
        print("To your left is a wooden chest")
        print("- Possible exit: nscorridor")
        state["looked_around"]["stairexit"] = True

    def handle_help():
        """Show help message with available commands."""
        print("\nAvailable commands:")
        if state["room_states"]["classroom2035"]["manifest"] is True:
            print("- manifest            : Check the manifest")
        if state["room_states"]["stairexit"]["chest_opened"] is False and state["looked_around"]["stairexit"] is True:
            print("- open chest          : See what’s in the chest.")
        if state["room_states"]["stairexit"]["chest_opened"] is False and state["looked_around"]["stairexit"] is True:
            print("--------------------------------------------------")
        elif state["room_states"]["classroom2035"]["manifest"] is True:
            print("--------------------------------------------------")
        print("- look around         : See what’s in the lobby.")
        print("- go nscorridor / back: Return to the main corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game.")
        print(f"\n- Your current health is {state["health"]} harts")
        print("- Your current inventory:", state["inventory"])

    def handle_go(destination):
        """Handle movement to another room."""
        if destination in ["nscorridor", "back"]:
            print("You leave the stair exit and head back into the nscorridor.")
            state["previous_room"] = "stairexit"
            return "nscorridor"
        else:
            print(f"You can't go to '{destination}' from here.")
            return None
    def handle_manifest():
        print("\nManifest:")
        for i in state["manifest"]:
            print(f"- name: {i}     gender: {state["manifest"][i]["gender"]}     age: {state["manifest"][i]["age"]}     favourite items: {state["manifest"][i]["item1"]}, {state["manifest"][i]["item2"]}, {state["manifest"][i]["item3"]}")
        print("\n To guess the ghost you need to tipe: are you (name)")

    # --- Main command loop ---

    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "open chest" and state["room_states"]["stairexit"]["chest_opened"] == False:
            print("\nYou open the chest and you have received bandages")
            print("When you use bandages you will gain 4 hearts")
            state["inventory"].append("bandages")
            print("\n- Your current inventory:", state["inventory"])
            state["room_states"]["stairexit"]["chest_opened"] = True

        elif command == "open chest" and state["room_states"]["stairexit"]["chest_opened"] == True:
            print("\nYou have already opened this chest")

        elif command == "?":
            handle_help()

        elif command == "manifest":
            handle_manifest()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("You suddenly explode. Game over.")
            sys.exit()

        else:
            print("Unknown command. Type '?' to see available commands.")
