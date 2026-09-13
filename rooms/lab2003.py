import sys, time


def enterLab2003(state):
    # --- Check if the player has the key to enter ---
    if not state["room_states"]["lab2003"]["door_unlocked"]:
        if "final key" not in state["inventory"]:
            print("\n🚪 The door to Lab 2003 is locked.")
            print("The door looks robust and high-tech. You might need a special key...")
            return "corridor"
        else:
            print("\nYou insert the final key into the lock and turn it.")
            print("WIP: description upon entering the room.")
            state["room_states"]["lab2003"]["door_unlocked"] = True
    else:
        print("WIP: description when you re-enter from corridor")
        # TODO: make it depend on lights on

    def handle_look():
        if not state["room_states"]["lab2003"]["lights_on"]:
            print("It's so dark in here that you can't see anything. Better turn the lights on...")
        else:
            print("WIP: description of the room when looking around.\n"
                  "You notice a person sitting at one of the desks...")
            state["looked_around"]["lab2001"] = True
        print("- Possible exits: corridor")
        print("- Your current inventory:", state["inventory"])
        # TODO: update new actions after looking
        if state["room_states"]["lab2003"]["lights_on"]:
            print("- New action available: approach the person")


    def handle_help():
        print("\nAvailable commands:")
        print("- look around         : Examine the room and its contents.")
        # TODO: add room-specific actions here!
        if not state["room_states"]["lab2003"]["lights_on"]:
            print("- lights on                : Turn on the lights.")
        elif state["looked_around"]["lab2001"]:
            print("- approach the person                : See if the person is okay.")
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

    def boss_battle():

        # boss fight functions
        def boss_attack():
            time.sleep(2)
            print("The boss attacks you!")
            state["room_states"]["lab2003"]["player_health"] -= 3
            display_health_bars()

        def player_attack():
            print("You punch the boss with your fist. Doesn't seem to do much...")
            state["room_states"]["lab2003"]["boss_health"] -= 1
            display_health_bars()

        def use_item():
            print("WIP!")
            # TODO: add code

        def display_health_bars():
            print("------------\n"
                  f"Boss HP: {state["room_states"]["lab2003"]["boss_health"]}\n"
                  f"Your HP: {state["room_states"]["lab2003"]["player_health"]}\n"
                  "------------\n")

        # solving the puzzle skips the fight
        print("WIP: you look at the person, it turns out to be a boss!")
        boss_answer = input("62656e206a696a2076696a616e64206f6620767269656e643f\n"
                            "> ").strip().lower()
        if boss_answer == "vriend" or boss_answer == "767269656e64":
            print("WIP: description of boss being nice and giving you the exit key.")
            state["inventory"].append("exit key")
            return

        # assuming wrong answer
        state["room_states"]["lab2003"]["boss_fight_active"] = True
        print("Look like the boss didn't like your answer. It's preparing to attack!")
        display_health_bars()

        # boss fight loop
        while state["room_states"]["lab2003"]["boss_health"] > 0:
            # boss attacks first
            boss_attack()

            # check if player's HP still positive after boss attack
            if state["room_states"]["lab2003"]["player_health"] <= 0:
                break

            # prompt player's action
            # - only actions: attack, use ...
            # print that any other action blocked during the fight
            command = input("What do you do!?\n"
                            "Available actions: punch, use <item>, quit\n"
                            "> ").strip().lower()

            if command == "punch":
                player_attack()

            if command.startswith("use "):
                # TODO: add handling
                use_item()

            elif command == "quit":
                # TODO: maybe adjust the message here
                print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
                sys.exit()

        print("WIP: what happens after the boss fight goes here")



        # TODO:
        #   - print boss description
        #   - print the riddle
        #   - change state to boss active
        #   - add boss active locks on other actions
        #   - set up fight parameters and inner functions
        #   - make a while loop - whoever drops first
        #   - add respawn mechanic

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

        elif command == "lights on":
            state["room_states"]["lab2003"]["lights_on"] = True
            print("You're dazzled by the bright lights. After a brief moment, your eyesight recovers.\n"
                  "Time to take a look around...")

        elif command == "approach the person":
            boss_battle()

        elif command == "quit":
            print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")