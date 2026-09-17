import sys
from .utils import chooseNextRoom

def enterProjectRoom1(state):
    print("\n🏫 You step into Project Room 1.")
    print("Suddenly, you find yourself floating. An endless sea of stars spreads out before you.")
    print("You turn and find you had just stepped out of an airlock.")

    def handle_look():
        print("\n The hyperdrive engine sits in a cuboid compartment beside the main engine.")
        print("It's quite small compared to the main engine.")
        print("You see several cylindrical, spherical, pyramid, and cube shapes.")
        print("You realize you're a computer scientist, not an engineer.")
        if not state["visited"]["projectroom1"]:
            #print("The teacher says, you are late! And he asks you a question:")
            #print("\"What is 7 * 6?\"")
            print('You see a compartment open that spherical objects flow out of.')
            print('You also see a cube connected by a cylindrical object. It may be out of place?')
            print('You can: 1. Clean up the spheres.')
            print('2. Replace the cube and cylinder.')
        else:
            #print("The teacher sighs: You again? You already solved the challenge.")
            print('The engine hums smoothly.')

            if "stardust_sphere" not in state["inventory"]:
                #print("On the desk, beneath the calculator, something metallic glints. It looks like a small key.")
                print('One of the spherical capsules seems to radiate a lot of heat.')
            else:
                #print("The desk is empty. You've already taken the key.")
                print('The compartment is clean and orderly.')
        print("- Possible exits: lobby")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        print("\nAvailable commands:")
        print("- look around         : Examine the room and its contents.")
        if not state["visited"]["projectroom1"]:
            #print("- answer <number>     : Attempt to solve the math question.")
            print("- action <number>     : Take a specific action to repair the engine.")
        if state["visited"]["projectroom1"] and "stardust sphere" not in state["inventory"]:
            print("- take stardust sphere            : Pick up the key once it's revealed.")
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")

    def handle_take(item):
        if item == "stardust sphere":
            if not state["visited"]["projectroom1"]:
                print("❌ There's no key visible yet. Maybe solving the puzzle will reveal more.")
                #print('unfinished')
            elif "stardust_sphere" in state["inventory"]:
                print("You already have the sphere in your inventory.")
                #print('unfinished')
            else:
                print("🔑 You lift the lone sphere.")
                print("It is suprisingly heavier than it looks. It\'s also quite warm.")
                print("You take it and tuck it safely into your backpack.")
                state["inventory"].append("stardust_sphere")
        else:
            print(f"There is no '{item}' here to take.")

    def handle_answer(answer):
        if state["visited"]["projectroom1"]:
            print("✅ You've already solved this challenge.")
        elif answer == "1":
            print("✅ Correct! Upon sorting the spheres, the engines sensors glow green.")
            state["visited"]["projectroom1"] = True
            print("Suddenly you see a single sphere you didn't see before.")
        else:
            print("❌ Incorrect. Upon disconnecting the cube, the engine immediately explodes.")
            print("You are forced back into the lobby.")
            return "lobby"

    def handle_go(destination):
        if destination in ["lobby", "back"]:
            print("🚪 You open the door and step back into the corridor.")
            return "lobby"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    #Main Classroom command loop
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command.startswith("take "):
            item = command[5:].strip()
            handle_take(item)

        elif command.startswith("go "):
            room = command[3:].strip()
            result = handle_go(room)
            if result:
                return result

        elif command.startswith("action "):
            answer = command[7:].strip()
            result = handle_answer(answer)
            if result:
                return result

        elif command == "quit":
            print("👋 You leave the school and the adventure comes to an end. Game over.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")