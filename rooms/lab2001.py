import sys
from strings import shared_strings as s, lab2001_strings as t

def enterLab2001(state):
    available_rooms = ["lobby"]
    print(t.ENTER_ROOM)

    def handle_look():
        print(t.LOOK_AROUND)
        print(s.POSSIBLE_EXITS.format(available_rooms=available_rooms))
        print(s.CURRENT_INVENTORY.format(inventory=state["inventory"]))
        print(t.NEW_ACTIONS)
        state["looked_around"]["lab2001"] = True

    def handle_help():
        print(s.COMMANDS_HEADER)
        if state["looked_around"]["lab2001"]:
            print(t.ROOM_SPECIFIC_COMMANDS["examine_workbench"])
            print(t.ROOM_SPECIFIC_COMMANDS["examine_notebook"])
        if state["room_states"]["lab2001"]["workbench_examined"]:
            print(t.ROOM_SPECIFIC_COMMANDS["set_resistance"])
            print(t.ROOM_SPECIFIC_COMMANDS["place_item"])
            print(t.ROOM_SPECIFIC_COMMANDS["run_workbench"])
            print(t.ROOM_SPECIFIC_COMMANDS["replace_laser"])
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

    def handle_examine(examined_object):
        if examined_object == "workbench":
            print(t.HANDLE_EXAMINE["workbench_desc"])
            # TODO: the setup params might need to be made global
            voltage = state["room_states"]["lab2001"]["given_voltage"]
            resistance = state["room_states"]["lab2001"]["resistance_setting"]
            print(t.WORKBENCH_SETTINGS["voltage"].format(voltage=voltage))
            print(t.WORKBENCH_SETTINGS["resistance"].format(resistance=resistance))
            print(t.HANDLE_EXAMINE["actions"])
            print(t.ROOM_SPECIFIC_COMMANDS["set_resistance"])
            print(t.ROOM_SPECIFIC_COMMANDS["place_item"])
            print(t.ROOM_SPECIFIC_COMMANDS["run_workbench"])
            print(t.ROOM_SPECIFIC_COMMANDS["replace_laser"])
            state["room_states"]["lab2001"]["workbench_examined"] = True
        elif examined_object == "notebook":
            print(t.HANDLE_EXAMINE["notebook_desc"])
            state["room_states"]["lab2001"]["notebook examined"] = True

    def handle_set_resistance(resistance):
        resistance = float(resistance)
        state["room_states"]["lab2001"]["resistance_setting"] = resistance
        print(t.HANDLE_SET_RESISTANCE.format(resistance=resistance))

    def handle_place_item(item):
        if item not in state["inventory"]:
            print(t.HANDLE_PLACE_ITEM["not_found"])
        else:
            if not item.startswith("key shard"):
                print(t.HANDLE_PLACE_ITEM["only_key_shards"])
            else:
                state["room_states"]["lab2001"]["key_shards_placed"][item] = True
                state["inventory"].remove(item)
                print(t.HANDLE_PLACE_ITEM["key_shard_placed"].format(item=item))

    def handle_run_workbench():
        # check if lab2003 key already forged
        if state["room_states"]["lab2001"]["lab2003_key_forged"]:
            print(t.HANDLE_RUN_WORKBENCH["already_forged"])
        # check if laser broken
        elif state["room_states"]["lab2001"]["laser_broken"]:
            print(t.HANDLE_RUN_WORKBENCH["laser_broken"])
        else:
            # check if all four key shards are on the plate
            if not all(value == True for value in state["room_states"]["lab2001"]["key_shards_placed"].values()):
                print(t.HANDLE_RUN_WORKBENCH["need_four_key_shards"])
            else:
                voltage = state["room_states"]["lab2001"]["given_voltage"]
                resistance = state["room_states"]["lab2001"]["resistance_setting"]
                print(t.WORKBENCH_SETTINGS["voltage"].format(voltage=voltage))
                print(t.WORKBENCH_SETTINGS["resistance"].format(resistance=resistance))
                electric_current = voltage / resistance
                supplied_power = voltage * electric_current
                # TODO: get max current from state
                if electric_current > 4.5:
                    state["room_states"]["lab2001"]["laser_broken"] = True
                    print(t.HANDLE_RUN_WORKBENCH["current_too_strong"])
                else:
                    #TODO: get min power from state
                    if supplied_power >= 1000:
                        state["inventory"].append("lab2003 key")
                        state["room_states"]["lab2001"]["lab2003_key_forged"] = True
                        print(t.HANDLE_RUN_WORKBENCH["forging_desc"])
                        # TODO: decide if we want to display inventory at this moment
                        print(s.CURRENT_INVENTORY.format(inventory=state["inventory"]))
                    else:
                        print(t.HANDLE_RUN_WORKBENCH["power_too_low"])

    def handle_replace_laser():
        # TODO: will need updating if action shown only when laser broken
        if not state["room_states"]["lab2001"]["laser_broken"]:
            print(t.HANDLE_REPLACE_LASER["already_fine"])
            return False
        else:
            print(t.HANDLE_REPLACE_LASER["fixing_laser"])
            return False

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

        elif command.startswith("examine "):
            examined_object = command[8:].strip()
            handle_examine(examined_object)

        elif command.startswith("set resistance to "):
            resistance = command[17:].strip()
            handle_set_resistance(resistance)

        elif command.startswith("place "):
            item = command[5:].strip()
            handle_place_item(item)

        elif command == "run workbench":
            handle_run_workbench()

        elif command == "replace laser":
            state["room_states"]["lab2001"]["laser_broken"] = handle_replace_laser()

        elif command == "quit":
            print(s.QUIT)
            sys.exit()

        else:
            print(s.UNKNOWN_COMMAND)
