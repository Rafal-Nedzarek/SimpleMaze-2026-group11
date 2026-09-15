import sys

def enterLab2001(state):
    print("Here goes the description of the room upon entering it.")

    def handle_look():
        print("You look around the room and see a workbench and a notebook on a table next to it.")
        print("- Possible exits: corridor")
        print("- Your current inventory:", state["inventory"])
        print("- New actions available: examine workbench, examine notebook")
        state["looked_around"]["lab2001"] = True

    def handle_help():
        print("\nAvailable commands:")
        print("- look around         : Examine the room and its contents.")
        # Add room-specific actions here!
        if state["looked_around"]["lab2001"]:
            print("- examine workbench               : Take a look at the workbench.")
            print("- examine notebook                : Look through the notebook.")
        if state["room_states"]["lab2001"]["workbench_examined"]:
            print("- set resistance to <number>  : Set the resistance on the workbench to a number of Ohms.\n"
                  "- place <item>                : Place a key shard on the workbench.\n"
                  "- run workbench               : Run the workbench laser.\n"
                  "- replace laser               : Replace the laser if it's broken.\n"
                  )
        # display take when the final key is ready
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")

    def handle_go(destination):
        if destination in ["corridor", "back"]:
            print("🚪 You open the door and step back into the corridor.")
            return "corridor"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    def handle_examine(examined_object):
        if examined_object == "workbench":
            print("You take a closer look at the workbench. It seems to be used for fusing things together.\n"
                  # TODO: update plate description to indicate key shards placed
                  "There is an empty, key-shaped plate in the middle of it.\n"
                  "The workbench has a laser head pointed towards the plate.\n"
                  # TODO: get minimum power and max current from state
                  "The laser has a \"Min power: 1000 W. Max current: 4.5 A\" label on it.\n"
                  "Next to the workbench is a huge box full of laser replacements.\n"
                  "Between the bench and the laser head you can see a potentiometer with a knob to adjust resistance.\n")
            # TODO: the setup params might need to be made global
            voltage = state["room_states"]["lab2001"]["given_voltage"]
            resistance = state["room_states"]["lab2001"]["resistance_setting"]
            print(f"Voltage: {voltage} Volt\n"
                  f"Resistance: {resistance} Ohm\n"
                  )
            print("You can:\n"
                  "- set resistance to <number>  : Set the resistance on the workbench to a number of Ohms.\n"
                  "- place <item>                : Place a key shard on the workbench.\n"
                  # TODO: consider showing the run command only after all key shards placed
                  "- run workbench               : Run the workbench laser.\n"
                  # TODO: consider showing replace laser only when laser is broken
                  "- replace laser               : Replace the laser if it's broken."
                  )
            state["room_states"]["lab2001"]["workbench_examined"] = True
        elif examined_object == "notebook":
            print("You look through a notebook placed on a table next to the workbench.\n"
                  "The latest entry is:\n"
                  "Power (Watts) = voltage (Volts) * current (Amps)\n"
                  "Current (Amps) = voltage (Volts) / resistance (Ohms)\n"
                  )
            state["room_states"]["lab2001"]["notebook examined"] = True

    def handle_set_resistance(resistance):
        resistance = float(resistance)
        state["room_states"]["lab2001"]["resistance_setting"] = resistance
        print(f"Resistance set to {state["room_states"]["lab2001"]["resistance_setting"]}")

    def handle_place_item(item):
        if item not in state["inventory"]:
            print("No such item in the inventory!")
        else:
            if not item.startswith("key shard"):
                print("This doesn't seem right. It looks like the plate is designed to handle only key shards.")
            else:
                state["room_states"]["lab2001"]["key_shards_placed"][item] = True
                state["inventory"].remove(item)
                print(f"You've placed {item} on the workbench plate.")

    def handle_run_workbench():
        # check if final key already forged
        if state["room_states"]["lab2001"]["final_key_forged"]:
            print("You've already forged the final key!")
        # check if laser broken
        elif state["room_states"]["lab2001"]["laser_broken"]:
            print("You need to replace the broken laser first!")
        else:
            # check if all four key shards are on the plate
            if not all(value == True for value in state["room_states"]["lab2001"]["key_shards_placed"].values()):
                print("All key shards need to be on the plate before you run the workbench!")
                # TODO: confirm if using break is better here
            else:
                # TODO: the setup params might need to be made global
                voltage = state["room_states"]["lab2001"]["given_voltage"]
                resistance = state["room_states"]["lab2001"]["resistance_setting"]
                print(f"Voltage: {voltage} Volt\n"
                      f"Resistance: {resistance} Ohm"
                      )
                electric_current = voltage / resistance
                supplied_power = voltage * electric_current
                # TODO: get max current from state
                if electric_current > 4.5:
                    state["room_states"]["lab2001"]["laser_broken"] = True
                    print("The current was too strong, the laser is broken now!\n"
                          "You need to replace the laser to continue."
                          # TODO: check notebook_examined from state
                          "The notebook might have some hints...")
                else:
                    #TODO: get min power from state
                    if supplied_power >= 1000:
                        state["inventory"].append("final key")
                        state["room_states"]["lab2001"]["final_key_forged"] = True
                        print("WIP: You watch the whole process...\n"
                              "You take the final key with you!")
                        # TODO: decide if we want to display inventory at this moment
                        print("- Your current inventory:", state["inventory"])
                    else:
                        print("The laser lights up but it has no effect on the four shards.\n"
                              "The supplied power must be too low...")

    def handle_replace_laser():
        # TODO: will need updating if action shown only when laser broken
        if not state["room_states"]["lab2001"]["laser_broken"]:
            print("The laser seems fine. No replacement needed.")
        else:
            state["room_states"]["lab2001"]["laser_broken"] = False
            print("You've replaced the laser with one of the lasers from the box.\n"
                  "You can use the workbench again!")

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
            result = handle_examine(examined_object)
            if result:
                return result

        elif command.startswith("set resistance to "):
            resistance = command[17:].strip()
            result = handle_set_resistance(resistance)
            if result:
                return result

        elif command.startswith("place "):
            item = command[5:].strip()
            result = handle_place_item(item)
            if result:
                return result

        elif command == "run workbench":
            result = handle_run_workbench()

        elif command == "replace laser":
            result = handle_replace_laser()

        elif command == "quit":
            print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")
