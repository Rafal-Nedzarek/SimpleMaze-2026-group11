# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

from rooms import enterCorridor, enterClassroom2015, enterNSCorridor, enterStairExit, enterLab2001

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
        # "classroom2031": False,
        # "classroom2035": False,
        "classroom2015": False,
        "projectroom3": False,
        "lab2001": False,
        "nscorridor": False,
        "stairexit": False,
        # "teachersroom4": False,
    },
    "inventory": []
}

while True:
    current = state["current_room"]

    if current == "corridor":
        state["current_room"] = enterCorridor(state)

    elif current == "nscorridor":
        state["current_room"] = enterNSCorridor(state)

    # elif current == "classroom2031":
    #     state["current_room"] = enterClassroom2031(state)
    #
    # elif current == "classroom2035":
    #     state["current_room"] = enterClassroom2035(state)

    elif current == "stairexit":
        state["current_room"] = enterStairExit(state)

    # elif current == "teachersroom4":
    #     state["current_room"] = enterTeachersRoom4(state)

    elif current == "classroom2015":
        state["current_room"] = enterClassroom2015(state)

    elif current == "lab2001":
        state["current_room"] = enterLab2001(state)


    else:
        print("Unknown room. Exiting game.")
        break
