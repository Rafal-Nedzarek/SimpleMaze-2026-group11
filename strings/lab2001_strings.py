ENTER_ROOM = ("You enter Lab 2001. The room is filled with PCs, cables, and all"
              " sorts of hardware. Nothing extraordinary at first glance.")
LOOK_AROUND = ("You look around the room. You notice an unfamiliar workbench and"
               " an open notebook on a table next to it.")
NEW_ACTIONS = "- New actions available: examine workbench, examine notebook"
ROOM_SPECIFIC_COMMANDS = {
    "examine_workbench": "- examine workbench               : Take a look at the workbench.",
    "examine_notebook": "- examine notebook                : Look through the notebook.",
    "set_resistance": "- set resistance to <number>  : "
                      "Set the resistance on the workbench to a number of Ohms.",
    "place_item": "- place <item>                : Place a key shard on the workbench.",
    "run_workbench": "- run workbench               : Run the workbench laser.",
    "replace_laser": "- replace laser               : Replace the laser if it's broken."
}
HANDLE_GO = {
    "valid": "You open the door and step back into the lobby.",
    "invalid": "You can't go to '{destination}' from here."
}
WORKBENCH_SETTINGS = {
    "voltage": "Voltage: {voltage} V",
    "resistance": "Resistance: {resistance} Ω",
}
HANDLE_EXAMINE = {
    "workbench_desc": ("You take a closer look at the workbench. It seems to be used for fusing things together.\n"
                  # TODO: update plate description to indicate key shards placed
                  "There is an empty, key-shaped plate in the middle of it.\n"
                  "The workbench has a laser head pointed towards the plate.\n"
                  # TODO: get minimum power and max current from state
                  "A label on the laser reads: \"Min power: 1000 W. Max current: 4.5 A.\"\n"
                  "Next to the workbench stands a huge box full of laser replacements.\n"
                  "Between the bench and the laser head you can see a potentiometer with a knob to adjust resistance.\n"),
    "actions": "\nYou can:",
    "notebook_desc": ("You look through a notebook placed on a table next to the workbench.\n"
                  "The latest entry reads:\n"
                  "----------------------------------------------------\n"
                  "Power (Watts) = voltage (Volts) * current (Amps)\n"
                  "Current (Amps) = voltage (Volts) / resistance (Ohms)\n"
                  "----------------------------------------------------")
}
HANDLE_SET_RESISTANCE = "Resistance set to {resistance} Ω."
HANDLE_PLACE_ITEM = {
    "not_found": "No such item in the inventory!",
    "only_key_shards": ("This doesn't seem right. It looks like the plate is "
                        "designed to handle only key shards."),
    "key_shard_placed": "You've placed {item} on the workbench plate."
}
HANDLE_RUN_WORKBENCH = {
    "already_forged": "You've already forged the lab2003 key!",
    "laser_broken": "You need to replace the broken laser first!",
    "need_four_key_shards": "All four key shards need to be on the plate before you run the workbench!",
    "current_too_strong": ("The current was too strong, the laser is broken now!\n"
                          "You need to replace the laser to continue. "
                          # TODO: check notebook_examined from state
                          "The notebook might have some hints..."),
    "forging_desc": ("You watch as the laser beam fuses the four key shards together.\n"
                              "You take the lab2003 key with you!"),
    "power_too_low": ("The laser lights up but has no effect on the four shards.\n"
                              "The supplied power must be too low...")
}
HANDLE_REPLACE_LASER = {
    "already_fine": "The laser seems fine. No replacement needed.",
    "fixing_laser": ("You've replaced the laser with one of the lasers from the box.\n"
                  "You can use the workbench again!")
}
