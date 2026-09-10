# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

from rooms import enterCorridor, enterStudyLandscape, enterClassroom2015, enterProjectRoom3, enterLab2001

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
    # TODO: consider moving this to room_states
    "looked_around": {
        "classroom2015": False,
        "projectroom3": False,
        "lab2001": False,
    },
    # dictionary for tracking room-specific states
    "room_states": {
        "lab2001": {
            "workbench_examined": False,
            "notebook_examined": False,
            "laser_broken": False,
            "resistance_setting": 0,
            "given_voltage": 230,
            "key_shards_placed": {
                "key shard 1": False,
                "key shard 2": False,
                "key shard 3": False,
                "key shard 4": False,
            },
            "final_key_forged": False,
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

    else:
        print("Unknown room. Exiting game.")
        break
