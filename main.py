# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

from rooms import enterCorridor, enterStudyLandscape, enterClassroom2015, enterProjectRoom3, enterLab2001, enterEnchantedLibrary

print("****************************************************************************")
print("*                      Welcome to the School Maze!                         *")
print("*        Your goal is to explore all important rooms in the school.        *")
print("*    You may need to solve challenges to collect items and unlock rooms.   *")
print("*               Once you've visited all rooms, you win!                    *")
print("****************************************************************************")

state = {
    "current_room": "corridor",
    "previous_room": "corridor",
    "visited": {
        "classroom2015": False,
        "projectroom3": False,
        "lab2001": False,
    },
    "room_states": {
        "enchanted_library":{
            "clue1_solved": False,
            "clue2_solved": False,
            "clue3_solved": False,
            "spellbook_unlocked": False,
        },
    },
    "inventory": []
}

while True:
    current = state["current_room"]

    if current == "corridor":
        state["current_room"] = enterCorridor(state)

    elif current == "studylandscape":
        state["current_room"] = enterStudyLandscape(state)

    elif current == "classroom2015":
        state["current_room"] = enterClassroom2015(state)

    elif current == "projectroom3":
        state["current_room"] = enterProjectRoom3(state)

    elif current == "lab2001":
        state["current_room"] = enterLab2001(state)

    elif current == "enchanted_library":
        state["current_room"] = enterEnchantedLibrary(state)

    else:
        print("Unknown room. Exiting game.")
        break
