# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

from rooms import enterCorridor, enterClassroom2015, enterNSCorridor, enterStairExit, enterLab2001, enterLab2003, enterEnchantedLibrary, enterteacherroom1, enterClassroom2031, enterClassroom2035, enterTeachersRoom4

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
        "nscorridor" : False,
        "classroom2031": False,
        "classroom2035": False,
        "stairexit": False,
        "teachersroom4": False,
    },

    "looked_around": {
        "classroom2031": False,
        "classroom2035": False,
        "stairexit": False,
        "teachersroom4": False,
        "classroom2015": False,
        "projectroom3": False,
        "lab2001": False,
        "lab2003": False,
        "nscorridor": False,
        "teacherroom1": False,
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
            "ghost discovered" : False
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
    "health" : 10,
    # TODO: make sure we have those items in other rooms, then clear inventory
    "inventory": ["playing cards", "notebook"],
    "hangman_words" : ["ghost", "haunt", "death", "skull", "grave", "night", "spook", "demon", "witch", "scary","dread",
                       "creep", "curse", "shade", "blood", "decay", "crypt", "ghoul", "abyss", "omens", "stalk", "burial",
                       "casket", "chills", "corpse", "creepy", "fright", "hollow", "horror", "lurker", "menace", "rotten",
                       "scream", "shadow", "shriek", "spider", "undead", "wicked", "zombie", "dungeon","haunted", "monster",
                       "ominous", "phantom", "possess", "severed", "stalker", "vampire", "whisper", "gloomy"],
    "manifest" : {
        "dominik" : {
            "age" : 21,
            "gender" : "male",
            "item1" : "playing cards",
            "item2" : "dog picture",
            "item3" : "photo camera"
        },
        "martin" : {
            "age" : 20,
            "gender" : "male",
            "item1" : "dog picture",
            "item2" : "playing cards",
            "item3" : "football"
        },
        "daniel" : {
            "age" : 21,
            "gender" : "male",
            "item1" : "playing cards",
            "item2" : "dog picture",
            "item3" : "football"
        },
        "vin": {
            "age": 20,
            "gender": "male",
            "item1": "notebook",
            "item2": "playing cards",
            "item3": "football"
        },
        "gabriel": {
            "age": 20,
            "gender": "male",
            "item1": "notebook",
            "item2": "dog picture",
            "item3": "football"
        },
        "johannes": {
            "age": 21,
            "gender": "male",
            "item1": "dog picture",
            "item2": "playing cards",
            "item3": "notebook"
        },
        "joseph": {
            "age": 21,
            "gender": "male",
            "item1": "dog picture",
            "item2": "photo camera",
            "item3": "notebook"
        },
        "david": {
            "age": 20,
            "gender": "male",
            "item1": "photo camera",
            "item2": "playing cards",
            "item3": "football"
        },
        "connor": {
            "age": 21,
            "gender": "male",
            "item1": "dog picture",
            "item2": "playing cards",
            "item3": "football"
        },
        "leon": {
            "age": 21,
            "gender": "male",
            "item1": "dog picture",
            "item2": "photo camera",
            "item3": "football"
        },
        "nick": {
            "age": 20,
            "gender": "male",
            "item1": "notebook",
            "item2": "photo camera",
            "item3": "football"
        },
        "damian": {
            "age": 20,
            "gender": "male",
            "item1": "notebook",
            "item2": "dog picture",
            "item3": "playing cards"
        },
        "stuart": {
            "age": 21,
            "gender": "male",
            "item1": "photo camera",
            "item2": "notebook",
            "item3": "football"
        },
        "mark": {
            "age": 21,
            "gender": "male",
            "item1": "notebook",
            "item2": "playing cards",
            "item3": "football"
        },
        "anett": {
            "age": 20,
            "gender": "female",
            "item1": "photo camera",
            "item2": "playing cards",
            "item3": "make-up"
        },
        "miina": {
            "age": 20,
            "gender": "female",
            "item1": "dog picture",
            "item2": "playing cards",
            "item3": "make-up"
        },
        "lisa": {
            "age": 20,
            "gender": "female",
            "item1": "playing cards",
            "item2": "notebook",
            "item3": "make-up"
        },
        "aria": {
            "age": 20,
            "gender": "female",
            "item1": "dog picture",
            "item2": "notebook",
            "item3": "make-up"
        },
        "veronika": {
            "age": 21,
            "gender": "female",
            "item1": "dog picture",
            "item2": "make-up",
            "item3": "playing cards"
        },
        "shelby": {
            "age": 21,
            "gender": "female",
            "item1": "notebook",
            "item2": "dog picture",
            "item3": "make-up"
        },
        "amy": {
            "age": 20,
            "gender": "female",
            "item1": "photo camera",
            "item2": "dog picture",
            "item3": "make-up"
        },
        "ashley": {
            "age": 21,
            "gender": "female",
            "item1": "photo camera",
            "item2": "notebook",
            "item3": "make-up"
        },
        "sara": {
            "age": 20,
            "gender": "female",
            "item1": "photo camera",
            "item2": "notebook",
            "item3": "playing cards"
        },
        "olivia": {
            "age": 21,
            "gender": "female",
            "item1": "photo camera",
            "item2": "dog picture",
            "item3": "make-up"
        },
        "elizabeth": {
            "age": 21,
            "gender": "female",
            "item1": "notebook",
            "item2": "photo camera",
            "item3": "make-up"
        },
        "kamila": {
            "age": 21,
            "gender": "female",
            "item1": "notebook",
            "item2": "dog picture",
            "item3": "playing cards"
        },

    },
}

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

    elif current == "classroom2015":
        state["current_room"] = enterClassroom2015(state)

    elif current == "lab2001":
        state["current_room"] = enterLab2001(state)

    # TODO: for all these calls, might be wasteful to send the whole state
    elif current == "lab2003":
        state["current_room"] = enterLab2003(state)

    elif current == "enchanted_library":
        state["current_room"] = enterEnchantedLibrary(state)

    elif current == "teacherroom1":
        state["current_room"] = enterteacherroom1(state)

    else:
        print("Unknown room. Exiting game.")
        break