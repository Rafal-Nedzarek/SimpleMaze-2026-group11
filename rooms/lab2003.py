import sys, time


def enterLab2003(state):
    # --- Check if the player has the key to enter ---
    if not state["room_states"]["lab2003"]["door_unlocked"]:
        if "lab2003 key" not in state["inventory"]:
            print("\n🚪 The door to Lab 2003 is locked.")
            print("The door looks robust and high-tech. You'll need a special key...")
            return "lobby"
        else:
            print("\nYou insert the lab2003 key into the lock and turn it.")
            print("As you enter the room, you're immediately enveloped with darkness.")
            state["room_states"]["lab2003"]["door_unlocked"] = True
    else:
        # door locked for good once lab2003 has been completed
        if state["visited"]["lab2003"]:
            print("You can't unlock the door anymore. The small screen next to the lock displays ERROR.")
            return "lobby"
        print("You re-enter Lab 2003.")
        if not state["room_states"]["lab2003"]["lights_on"]:
            print("You can't see anything in the darkness.")

    def handle_look():
        if not state["room_states"]["lab2003"]["lights_on"]:
            print("It's so dark in here that you can't see anything. Better turn the lights on first...")
        else:
            print("You look around the room and notice one desk placed exactly in the middle.\n"
                  "Around the desk a group of small, tracked robots are busy placing candles around the place.\n"
                  "It seems they're preparing some sort of ritual. Your attention moves onto the desk.\n"
                  "You notice a hooded person sitting at the desk...")
            state["looked_around"]["lab2001"] = True
        print("- Possible exits: lobby")
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
        print("- go lobby / back  : Leave the room and return to the lobby.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")

    def handle_go(destination):
        if destination in ["lobby", "back"]:
            print("🚪 You open the door and step back into the lobby.")
            return "lobby"
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
        print("You approach the hooded person. You notice they're wearing long, crimson robes.\n"
              "You can't clearly see their face, but you see some cables sticking out from beneath the robes.\n"
              "The pair of eyes glowing under the hood turns towards you. You hear what sounds like a question:")
        boss_answer = input("62656e206a696a2076696a616e64206f6620767269656e643f\n"
                            "> ").strip().lower()
        if boss_answer == "vriend" or boss_answer == "767269656e64":
            print("The person nods their hooded head. You could swear you hear the buzzing of servo motors under those robes.\n"
                  "The person extends their robotic hand with a key, you take it in silence.\n"
                  "Not sure what to make of all that, you quickly go back to the lobby.")
            state["inventory"].append("exit key")
            state["visited"]["lab2003"] = True
            return "lobby"

        # assuming wrong answer
        state["room_states"]["lab2003"]["boss_fight_active"] = True
        print("Looks like the person didn't like your answer. They stand up and grab a two-handed axe that was hidden among the lab's hardware.\n"
              "The eyes under the hood glow ominously, the servo motors under the robes are abuzz. They're preparing to attack!")
        display_health_bars()

        # boss fight loop
        while state["room_states"]["lab2003"]["boss_health"] > 0:
            # boss attacks first
            boss_attack()

            # check if player's HP still positive after boss attack
            if state["room_states"]["lab2003"]["player_health"] <= 0:
                print("You've been defeated! You use your last strength to reach into your pocket.\n"
                      "You pop a paracetamol pill to revive yourself. After a while you wake up in the lobby.")
                return "lobby"

            # prompt player's action
            # - only actions: attack, use ...
            # print that any other action blocked during the fight
            command = input("What do you do!?\n"
                            # Hide use <item> action while under construction
                            # "Available actions: punch, use <item>, quit\n"
                            "Available actions: punch, quit\n"
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
            result = boss_battle()
            if result:
                return result

        elif command == "quit":
            print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")