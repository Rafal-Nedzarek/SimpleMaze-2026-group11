import sys
from .utils import chooseNextRoom

def enterLobby(state):
    print("\n🛋️ The lobby opens up to you.")
    print("You hear the hum of the ventilation and the coffee machine.")
    print("A screen flickers above you.")

    # --- List of accessible rooms from here ---
    available_rooms = ["corridor", "projectroom1", "projectroom2", "lab2001", "exit"]

    def handle_look():
        """Describe the lobby and show exits."""
        print("\nYou take a slow look around.")
        print("There are a few posters on the wall about upcoming student events.")
        print("A group of students is sitting in the corner gazing at a laptop")

        #Decide setting, and decide how exits are done
        print(f"- Possible doors: {', '.join(available_rooms)}")
        print("- Your current inventory:", state["inventory"])

    def handle_help():
        """List available commands and explain navigation."""
        print("\nAvailable commands:")
        print("- look around         : See what's in the corridor and where you can go.")
        print("- go <room name>      : Move to another room. Example: go classroom2015")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game.")

    def handle_go(room_name):
        """Move to a listed room."""
        room = room_name.lower()
        if room in available_rooms:
            print(f"You walk toward the door to {room}.")
            state["previous_room"] = "lobby"
            return room
        else:
            print(f"❌ '{room_name}' is not a valid exit. Use 'look around' to see available options.")
            return None

# --- Main lobby command loop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            room = command[3:].strip()
            result = handle_go(room)
            if result:
                return result

        elif command == "quit":
            print("👋 You leave the school and the adventure comes to an end. Game over.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")