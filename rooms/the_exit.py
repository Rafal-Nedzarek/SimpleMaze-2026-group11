import sys
from .utils import chooseNextRoom

def enterTheExit(state):
    # --- Check if the player has the key to enter ---
    # TODO: add hints on where to go
    if "exit key" not in state["inventory"]:
        print("\n🚪 The door to the exit  is locked.")
        print("You jiggle the handle. It's no use.")
        print("🔐 You need a key. Perhaps it's hidden elsewhere in the school?")
        return "lobby"
    else:
        print("\n🗝️ You insert the brass key into the lock and turn it with a satisfying click.")
        print("The door creaks open to reveal a stairwell leading outside.")
        print("Congratulations! You completed the game.")
        sys.exit()