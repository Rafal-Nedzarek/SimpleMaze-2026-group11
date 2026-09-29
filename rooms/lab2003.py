import sys, time
from strings import shared_strings as s, lab2003_strings as t

def enterLab2003(state):
    available_rooms = ["lobby"]
    # --- Check if the player has the key to enter ---
    if not state["room_states"]["lab2003"]["door_unlocked"]:
        if "lab2003 key" not in state["inventory"]:
            print(t.DOOR_LOCKED)
            return "lobby"
        else:
            print(t.DOOR_UNLOCKED)
            print(t.ENTER_ROOM)
            state["room_states"]["lab2003"]["door_unlocked"] = True
    else:
        # door locked for good once lab2003 has been completed
        if state["visited"]["lab2003"]:
            print(t.DOOR_LOCKED_END)
            return "lobby"
        print(t.RE_ENTER_ROOM)
        if not state["room_states"]["lab2003"]["lights_on"]:
            print(t.LIGHTS_OFF)

    def handle_look():
        if not state["room_states"]["lab2003"]["lights_on"]:
            print(t.LIGHTS_OFF)
        else:
            print(t.LOOK_AROUND)
            state["looked_around"]["lab2001"] = True
        print(s.POSSIBLE_EXITS.format(available_rooms=available_rooms))
        print(s.CURRENT_INVENTORY.format(inventory=state["inventory"]))
        if state["room_states"]["lab2003"]["lights_on"]:
            print(t.NEW_ACTIONS)


    def handle_help():
        print(s.COMMANDS_HEADER)
        if not state["room_states"]["lab2003"]["lights_on"]:
            print(t.ROOM_SPECIFIC_COMMANDS["lights_on"])
        elif state["looked_around"]["lab2001"]:
            print(t.ROOM_SPECIFIC_COMMANDS["approach"])
        print(s.STANDARD_COMMANDS["look_around"])
        print(s.STANDARD_COMMANDS["go_back"])
        print(s.STANDARD_COMMANDS["help"])
        print(s.STANDARD_COMMANDS["quit"])

    def handle_go(destination):
        if destination in ["lobby", "back"]:
            print(t.HANDLE_GO["valid"])
            return "lobby"
        else:
            print(t.HANDLE_GO["invalid"].format(destination=destination))
            return None

    def boss_battle():

        # boss fight functions
        def boss_attack():
            time.sleep(2)
            print(t.BOSS_FIGHT["enemy_attacks"])
            state["health"] -= 3
            display_health_bars()

        def player_attack():
            print(t.BOSS_FIGHT["player_punch"])
            state["room_states"]["lab2003"]["boss_health"] -= 1
            display_health_bars()

        def display_health_bars():
            print(t.BOSS_FIGHT["health_bars"].format(
                boss_health=state["room_states"]["lab2003"]["boss_health"],
                player_health=state["health"]
            ))

        # solving the puzzle skips the fight
        print(t.BOSS_CONVERSATION["boss_desc"])
        boss_answer = input(t.BOSS_CONVERSATION["boss_question"]).strip().lower()
        if boss_answer == "vriend" or boss_answer == "767269656e64":
            print(t.BOSS_CONVERSATION["answer_correct"])
            state["inventory"].append("exit key")
            state["visited"]["lab2003"] = True
            return "lobby"

        # assuming wrong answer
        state["room_states"]["lab2003"]["boss_fight_active"] = True
        print(t.BOSS_CONVERSATION["answer_wrong"])
        display_health_bars()

        # boss fight loop
        while state["room_states"]["lab2003"]["boss_health"] > 0:
            # boss attacks first
            boss_attack()

            # check if player's HP still positive after boss attack
            if state["health"] <= 0:
                print(t.BOSS_FIGHT["player_lost"])
                return "lobby"

            # prompt player's action
            # - only actions: attack, use ...
            # print that any other action blocked during the fight
            command = input(t.BOSS_FIGHT["available_actions"]).strip().lower()

            if command == "punch":
                player_attack()

            if command.startswith("use "):
                item = command[4:]
                if item in state["inventory"]:
                    if item == "bandages":
                        heal = 4
                        state["health"] = state["health"] + heal if state["health"] + heal < 10 else 10
                        print(t.BOSS_FIGHT["player_heal"].format(heal=heal))
                        display_health_bars()
                    # TODO: replace the placeholders below with actual weapon/item names
                    elif item in ["special weapon 1", "special weapon 2", "special weapon 3"]:
                        special_weapon_dmg = 34
                        state["room_states"]["lab2003"]["boss_health"] -= special_weapon_dmg
                        print(t.BOSS_FIGHT["item_attack"].format(
                            special_weapon_dmg=special_weapon_dmg
                        ))
                        # NOTE: making those special weapons one use only
                        # that way you'll need all three instead of reusing just one
                        state["inventory"].remove(item)
                        print(t.BOSS_FIGHT["item_removed"].format(item=item))
                    else:
                        print(t.BOSS_FIGHT["item_useless"])
                else:
                    print(t.BOSS_FIGHT["item_not_found"])

            elif command == "rage quit":
                print(t.BOSS_FIGHT["rage_quit"])
                sys.exit()

            else:
                print(t.BOSS_FIGHT["unknown_command"])

        time.sleep(2)
        print(t.BOSS_FIGHT["boss_defeated"])
        state["inventory"].append("exit key")
        state["visited"]["lab2003"] = True
        time.sleep(2)
        return "lobby"

    # --- Commandoloop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "lights on" and not state["room_states"]["lab2003"]["lights_on"]:
            state["room_states"]["lab2003"]["lights_on"] = True
            print(t.LIGHTS_ON)

        elif command == "approach the person":
            result = boss_battle()
            if result:
                return result

        elif command == "quit":
            print(s.QUIT)
            sys.exit()

        else:
            print(s.UNKNOWN_COMMAND)