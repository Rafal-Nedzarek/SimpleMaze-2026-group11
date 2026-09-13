# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

from rooms import enterCorridor, enterClassroom2015, enterNSCorridor, enterStairExit, enterLab2001, enterLab2003, enterEnchantedLibrary

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
        "lab2003": False,
        "nscorridor": False,
        "stairexit": False,
        # "teachersroom4": False,
    },
    # TODO: consider moving this to room_states
    "looked_around": {
        "classroom2015": False,
        "projectroom3": False,
        "lab2001": False,
        "lab2003": False,
    },
    # dictionary for tracking room-specific states
    "room_states": {
        "stairexit": {
          "opened_chest": False,
        },
        "enchanted_library":{
            "clue1_solved": False,
            "clue2_solved": False,
            "clue3_solved": False,
            "spellbook_unlocked": False,
        },
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
        "lab2003": {
            "door_unlocked": False,
            "lights_on": False,
            "boss_fight_active": False,
            "player_health": 10,
            "boss_health": 100,
        },
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

    # TODO: for all these calls, might be wasteful to send the whole state
    elif current == "lab2003":
        state["current_room"] = enterLab2003(state)

    elif current == "enchanted_library":
        state["current_room"] = enterEnchantedLibrary(state)

    else:
        print("Unknown room. Exiting game.")
        break
