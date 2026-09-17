import sys
from .utils import chooseNextRoom

def enterProjectRoom2(state):
    print('"All combatants, report to battle stations."')
    print("You find yourself in some sort of base. However, the surroundings outside look alien.")
    print("You are in some sort of artillery station with a chair to control a mounted turret.")

    # --- Helperfuncties voor commandoverwerking ---

    def handle_look():
        print("\nYou take a careful look in the viewport.")
        #print("You see two groups of squid looking aliens. A larger and a smaller group.")
        #print("Desks with students are arranged in neat rows, though one chair is oddly turned toward the window.")
        #print("On the teacher's desk, a calculator is lying in a strange position on the table.")
        if not state["visited"]["projectroom2"]:
            print("You see two groups of squid looking aliens. A larger and a smaller group.")
            #print("\"What is 7 * 6?\"")
            print('Which group do you target?')
        else:
            #print("The teacher sighs: You again? You already solved the challenge.")
            if "key" not in state["inventory"]:
                #print("On the desk, beneath the calculator, something metallic glints. It looks like a small key.")
                print("The alien part on the floor writhes. It looks like it might be useful.")
            else:
                print("There is nothing more you can do here.")
        print("- Possible exits: lobby")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        print("\nAvailable commands:")
        print("- look around         : Examine the room and its contents.")
        if not state["visited"]["projectroom2"]:
            print("- target <group>     : Target the 'larger' or 'smaller' group.")
        if state["visited"]["projectroom2"] and "key" not in state["inventory"]:
            print("- take tentacle            : Pick up the key once it's revealed.")
        print("- go lobby / back  : Leave the room and return to the lobby.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")

#Come back here later
    def handle_take(item):
        if item == "tentacle":
            if not state["visited"]["projectroom2"]:
                print("❌ There's no key visible yet. Maybe solving the puzzle will reveal more.")
            elif "key" in state["inventory"]:
                print("You already have the key in your backpack.")
            else:
                print("🔑 You extract the part from the broken viewport.")
                print("You take it and tuck it safely into your backpack.")
                state["inventory"].append("tentacle")
        else:
            print(f"There is no '{item}' here to take.")

    def handle_go(destination):
        if destination in ["lobby", "back"]:
            print("🚪 You open the door and step back into the lobby.")
            return "lobby"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    def handle_answer(answer):
        if state["visited"]["projectroom2"]:
            #print("✅ You've already solved this challenge.")
            print("Despite the alarm, the battlefield is quiet.")
        elif answer == "smaller":
            print("✅ Correct! You shoot and take down the smaller group.")
            print("✅ The larger group gets obliterated by a fusion bomb from elsewhere.")
            state["visited"]["projectroom2"] = True
            print("A piece of the alien flies into your viewport and breaks the glass.")
        elif answer == "larger":
            print("❌ A fusion bomb is launched at the larger group.")
            print("The smaller group charges at the base.")
            print("You run into the door before they reach you.")
            return "lobby"
        else:
            print("❌ Invalid answer.")


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
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command.startswith("target "):
            answer = command[7:].strip()
            result = handle_answer(answer)
            if result:
                return result

        elif command == "quit":
            print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")
