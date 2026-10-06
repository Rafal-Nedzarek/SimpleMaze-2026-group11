# -----------------------------------------------------------------------------
# File: teachersroom4.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

import sys
from data import MANIFEST
from functions import shared_functions as sf
from rooms.utils import healing


def enterTeachersRoom4(state):

    print("\nYou step into Teachers room 4.")
    if state["visited"]["teachersroom4"] is False:
        print("The room has a flickering light and papers are all over the ground")
        print("there is broken glass on the ground")
    state["visited"]["teachersroom4"] = True

    # --- Command handlers ---

    def handle_look():
        """Describe the room and give clues."""
        print("\nYou scan the room.")
        print("There is a table on which is a broken laptop, some office supplies, mug and calendar")
        print("On the wall is a broken clock")
        print("behind the table is a safe")
        print("- Possible exits: nscorridor")
        print("- Your current inventory:", state["inventory"])
        state["looked_around"]["teachersroom4"] = True

    def handle_help():
        """List available commands."""
        print("\nAvailable commands:")
        if state["room_states"]["classroom2035"]["manifest"] is True:
            print("- manifest            : Check the manifest")
        if state["looked_around"]["teachersroom4"] is True:
            if state["room_states"]["teachersroom4"]["safe_opened"] is False or state["room_states"]["teachersroom4"]["mug"] is False or state["room_states"]["teachersroom4"]["calendar"] is False or state["room_states"]["teachersroom4"]["clock"] is False:
                print("- check              : Check some areas of the room")
                if state["room_states"]["teachersroom4"]["safe_opened"] is False:
                    print("      ‣ safe          : Check the safe")
                if state["room_states"]["teachersroom4"]["mug"] is False and state["room_states"]["teachersroom4"]["safe"] is True:
                    print("      ‣ mug           : Check the mug")
                if state["room_states"]["teachersroom4"]["calendar"] is False and state["room_states"]["teachersroom4"]["safe"] is True:
                    print("      ‣ calendar      : Check the calendar")
                if state["room_states"]["teachersroom4"]["clock"] is False and state["room_states"]["teachersroom4"]["safe"] is True:
                    print("      ‣ clock         : Check the clock")
            if state["room_states"]["teachersroom4"]["mug"] is True and state["room_states"]["teachersroom4"]["safe_opened"] is False:
                print("- roman numbers       : Cheat sheet for roman numbers")
            if state["looked_around"]["teachersroom4"] is True and state["room_states"]["teachersroom4"]["safe_opened"] is False or state["room_states"]["classroom2035"]["manifest"] is True:
                print("--------------------------------------------------")
            elif state["room_states"]["classroom2035"]["manifest"] is True:
                print("--------------------------------------------------")
        print("- use bandages        : Use bandages to heal 4 harts.")
        print("- look around         : Examine the room for clues.")
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game completely.")
        print(f"\n- Your current health is {state["health"]} harts")
        print("- Your current inventory:", state["inventory"])

    def handle_go(destination):
        """Handle movement out of the room."""
        if destination in ["nscorridor", "back"]:
            print("You step away from the lively room and return to the nscorridor.")
            state["previous_room"] = "teachersroom4"
            return "nscorridor"
        else:
            print(f"You can't go to '{destination}' from here.")
            return None

    def handle_check(item):
        try:
            room = state["room_states"]["teachersroom4"]

            if item == "safe":
                if room["safe"] is True and room["safe_opened"] is True:
                    print("Safe is opened, there is nothing else to do.")
                elif room["safe"] is False and room["safe_opened"] is False:
                    print("You go closer to a safe")
                    print("You try to open it but it's closed and the safe is asking a code from you.")
                    print("You notice that on the side of the safe is a sticky note.")
                    print("\nstickynote: 📅 + 🕕 + 🍵 = 🖥❓")
                    print("\nYou step away from the safe")
                    room["safe"] = True
                elif room["safe"] is True and room["safe_opened"] is False:
                    print("You go closer to a safe")
                    password = input("\nEnter 4 digits password: ").strip()
                    try:
                        if len(password) != 4:
                            raise ValueError
                        int(password)  # raises ValueError if it contains non-digits
                    except ValueError:
                        print("The password must be exactly 4 digits.")
                        return

                    if password == "5478":
                        print("\nYou open the safe.")
                        print("\nInside of the safe is a photo camera and a make-up kit")
                        state["inventory"].append("photo camera")
                        state["inventory"].append("make-up")
                        print("\n- Your current inventory:", state["inventory"])
                        room["safe_opened"] = True
                        state["room_states"]["classroom2031"]["photo camera"] = True
                        state["room_states"]["classroom2031"]["make-up"] = True
                    else:
                        print("Invalid password.")

            elif item == "calendar":
                if room["calendar"] is True:
                    print("There is nothing new, 31st of October is still circled")
                else:
                    print("You look at the calendar at the desk")
                    print("You can see that 31st of October is circled and stuck in the calendar is a picture of a dog")
                    state["inventory"].append("dog picture")
                    print("\n- Your current inventory:", state["inventory"])
                    room["calendar"] = True
            elif item == "clock":
                if room["clock"] is True:
                    print("The clock still shows 6:06")
                else:
                    print("You look at the broken clock on a wall")
                    print("It says 6:06")
                    room["clock"] = True

            elif item == "mug":
                if room["mug"] is not True:
                    print("You look at the mug on a desk")
                    room["mug"] = True
                print("On the mug is the Trevi Fountain and under it are the roman numerals MDCCLXII")

            else:
                print("Unknown object.")

        except KeyError as e:
            print(f"Error: missing game data {e}. Check that it exists in state.")

    def handle_manifest():
        print("\nManifest:")
        for i in MANIFEST:
            print(f"- name: {i}     gender: {MANIFEST[i]["gender"]}     age: {MANIFEST[i]["age"]}     favourite items: {MANIFEST[i]["item1"]}, {MANIFEST[i]["item2"]}, {MANIFEST[i]["item3"]}")
        print("\n To guess the ghost you need to tipe: are you (name)")

    # --- Main command loop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command == "roman numbers":
            print("\nThe roman numbers are:")
            print("I = 1")
            print("V = 5")
            print("X = 10")
            print("L = 50")
            print("C = 100")
            print("D = 500")
            print("M = 1000")

        elif command.startswith("check"):
            item = command[12:].strip()
            handle_check(item)

        elif command == "manifest":
            handle_manifest()

        elif command == "use bandages":
            if "bandages" in state["inventory"]:
                healing(state)
            else:
                print("You don't have any bandages.")

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("You close your notebook and leave the project behind. Game over.")
            sys.exit()

        elif command == "status":
            sf.show_completion(state["completed"])

        else:
            print("Unknown command. Type '?' to see available commands.")