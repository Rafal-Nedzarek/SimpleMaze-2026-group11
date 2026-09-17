
# -----------------------------------------------------------------------------
# File: projectroom3.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------
#
import sys
from .utils import chooseNextRoom

def enterProjectRoom3(state):
    print("\n🏫 You step Project Room 3.")
    print("You find yourself in a large room that is built with hardened clay bricks.")
    print("The top of the room has an open section, seeing the stars.")

    # --- Helperfuncties voor commandoverwerking ---

    def handle_look():
        print("\nYou take a careful look around the room.")
        print("It appears to be some kind of observatory.")
        print("Constellation diagrams line the walls of the room.")
        #print("On the teacher's desk, a calculator is lying in a strange position on the table.")
        if not state["visited"]["projectroom3"]:
            print("There is an instrument in the center of the room.")
            #print("\"What is 7 * 6?\"")
            print("On a circular face, it contains the names of animals: ")
            print("Rat, Ox, Tiger, Rabbit, <empty>, Snake, Horse, Goat, Monkey, Rooster, Pig.")
            print("It seems one of the inscriptions is missing.")
        else:
            #print("The teacher sighs: You again? You already solved the challenge.")
            print('The incriptions glow.')
            if "astrolabe" not in state["inventory"]:
                print("On the central table, a smaller instrument popped out.")
            else:
                print("The table and the observatory turn slowly. You've already taken the astrolabe.")
        print("- Possible exits: corridor")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        print("\nAvailable commands:")
        print("- look around         : Examine the room and its contents.")
        if not state["visited"]["projectroom3"]:
            print("- inscribe <animal>     : Figure out the missing animal(?)")
        if state["visited"]["projectroom3"] and "key" not in state["inventory"]:
            print("- take astrolabe            : Pick up the astrolabe once it's revealed.")
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")

    def handle_take(item):
        if item == "astrolabe":
            if not state["visited"]["projectroom3"]:
                print("❌ There's no key visible yet. Maybe solving the puzzle will reveal more.")
            elif "astrolabe" in state["inventory"]:
                print("You already have the astrolabe in your backpack.")
            else:
                print("🔑 You lift the astrolabe from the table.")
                print("You take it and tuck it safely into your backpack.")
                state["inventory"].append("astrolabe")
        else:
            print(f"There is no '{item}' here to take.")

    def handle_go(destination):
        if destination in ["corridor", "back"]:
            print("🚪 You open the door and step back into the corridor.")
            return "corridor"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    def handle_answer(answer):
        if state["visited"]["projectroom3"]:
            print("✅ You've already solved this challenge.")
        elif answer == "Dragon":
            print("✅ Correct! The table glows, and the entire room starts to turn around you.")
            state["visited"]["projectroom3"] = True
            print("Suddenly you see something pop out of the center.")
        else:
            print("❌ Incorrect. Mysteriously, the inscription you wrote disappears.")

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
