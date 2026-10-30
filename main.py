# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------
from functions.shared_functions import read_save_file
from functions.login_functions import getUser
from functions import shared_functions as sf

from rooms import (
    enterCorridor,
    enterNSCorridor,
    enterStairExit,
    enterLab2003,
    enterEnchantedLibrary,
    enterteacherroom1,
    enterClassroom2031,
    enterClassroom2035,
    enterTeachersRoom4,
    enterLobby,
    enterProjectRoom1,
    enterProjectRoom2,
    enterProjectRoom3,
    enterTheExit,
    enterexamroom,
    enterBreakRoom,
    enterDragonsLeftHand,
    enterDragonKnightRoom
)

state = {
    "user_name": None,
    "total_playtime": 0,
    "current_room": "corridor",
    "previous_room": "corridor",
    "visited": {
        "corridor" : False,
        "nscorridor" : False,
        "classroom2031": False,
        "classroom2035": False,
        "stairexit": False,
        "teachersroom4": False,
        "projectroom1": False,
        "projectroom2": False,
        "projectroom3": False,
        "lab2003": False,
        "examroom": False,
    },

    "completed": {
        "break_room" : False,
        "classroom2031" : False,
        "classroom2035": False,
        "enchanted_library" : False,
        "lab2001": False,
        "lab2003": False,
        "projectroom1": False,
        "projectroom2": False,
        "projectroom3": False,
        "stairexit" : False,
        "teacherroom1" : False,
        "teachersroom4" : False,
        "dragons_left_hand" : False,
        "dragons_knight_room" : False,
        "examroom" : False,
    },

    "section_finished":{
        "medieval": True,
        "chinese": True,
        "scifi": True,
        "horror": False,
        "boss": True,
    },
    "looked_around": {
        "classroom2031": False,
        "classroom2035": False,
        "stairexit": False,
        "teachersroom4": False,
        "classroom2015": False,
        "projectroom2": False,
        "projectroom3": False,
        "lab2001": False,
        "lab2003": False,
        "nscorridor": False,
        "teacherroom1": False,
        "examroom": False,
    },
    # dictionary for tracking room-specific states
    "room_states": {
        "stairexit": {
            "chest_opened": False,
        },
        "classroom2035": {
            "folder" : False,
            "manifest" : False,
            "desk" : False,
            "board" : False,
            "game_over" : False,
            "football" : False,
            "crucifix" : False,
            "wrong_guess" : 0,
            "guessed_letters" : []
        },
        "teachersroom4": {
            "safe" : False,
            "safe_opened" : False,
            "mug" : False,
            "calendar" : False,
            "clock" : False,
        },
        "classroom2031": {
            "playing cards" : False,
            "dog picture" : False,
            "photo camera" : False,
            "football" : False,
            "notebook" : False,
            "make-up" : False,
            "ghost discovered" : False,
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
            "lab2003_key_forged": False,
        },
        "lab2003": {
            "door_unlocked": False,
            "lights_on": False,
            "boss_fight_active": False,
            "boss_health": 100,
        },
    },
    "health" : 10,
    "inventory": [],
}

user_name = getUser()
state["user_name"] = user_name
sf.intro()

save_state = read_save_file(user_name)

if save_state is None:
    pass
else:
    state = save_state

while True:
    current = state["current_room"]

    if current == "corridor":
        state["current_room"] = enterCorridor(state)

    elif current == "nscorridor":
        state["current_room"] = enterNSCorridor(state)

    elif current == "classroom2031":
        state["current_room"] = enterClassroom2031(state)

    elif current == "classroom2035":
        state["current_room"] = enterClassroom2035(state)

    elif current == "stairexit":
        state["current_room"] = enterStairExit(state)

    elif current == "teachersroom4":
        state["current_room"] = enterTeachersRoom4(state)

    # Jason room functionality changes
    elif current == "lobby":
        state["current_room"] = enterLobby(state)

    elif current == "projectroom1":
        state["current_room"] = enterProjectRoom1(state)

    elif current == "projectroom2":
        state["current_room"] = enterProjectRoom2(state)

    elif current == "projectroom3":
        state["current_room"] = enterProjectRoom3(state)

    elif current == "the_exit":
        state["current_room"] = enterTheExit(state)

    elif current == "lab2003":
        state["current_room"] = enterLab2003(state)

    elif current == "enchanted_library":
        state["current_room"] = enterEnchantedLibrary(state)

    elif current == "break_room":
        state["current_room"] = enterBreakRoom(state)

    elif current == "teacherroom1":
       state["current_room"] = enterteacherroom1(state)

    elif current == "examroom":
        state["current_room"] = enterexamroom(state)

    elif current == "dragons_left_hand":
        state["current_room"] = enterDragonsLeftHand(state)

    elif current == "dragon_knight_room":
        state["current_room"] = enterDragonKnightRoom(state)

    else:
        print("Unknown room. Exiting game.")
        break