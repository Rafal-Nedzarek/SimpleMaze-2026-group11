def get_room_state(state):
    """Get or initialize the persistent state of The Dark Night."""
    state.setdefault("inventory", [])
    state.setdefault("completed", {})
    state.setdefault("room_states", {})

    return state["room_states"].setdefault(
        "break_room",
        {
            "sun_touched": False,
            "puzzle_solved": False,
            "reward_claimed": False,
            "attempts": 0,
            "energy": 0,
        },
    )


def ask_choice(prompt, valid_choices):
    """Ask until the player enters a valid choice."""
    valid_choices = [choice.lower() for choice in valid_choices]

    while True:
        answer = input(prompt).strip().lower()

        if answer in valid_choices:
            return answer

        print(f"Invalid choice. Choose: {', '.join(valid_choices)}")


def show_status(room):
    """Display the Dark Sun's current energy."""
    print("\n========== DARK SUN STATUS ==========")
    print(f"Energy collected: {room['energy']}/30")

    if room["puzzle_solved"]:
        print("Puzzle: SOLVED")
    else:
        print("Puzzle: UNSOLVED")

    print("=====================================")


def interact_with_sun(room):
    """Let the player interact with the Dark Sun once."""
    if room["sun_touched"]:
        print("\nThe Dark Sun recognizes you.")
        print("Its purple light pulses gently.")
        return

    print("\nThe Dark Sun floats in front of you.")
    print("Its surface contains three glowing symbols.")
    print("You can feel energy coming from it.")

    choice = ask_choice(
        "\n1. Touch the Dark Sun\n"
        "2. Observe it carefully\n"
        "Choose: ",
        ["1", "2"],
    )

    if choice == "1":
        print("\nYou touch the Dark Sun!")
        print("A wave of purple energy surrounds you.")
        room["energy"] += 15
    else:
        print("\nYou observe the symbols without touching them.")
        print("You discover a small inscription.")
        print('"Light reveals what darkness hides."')
        room["energy"] += 10

    room["sun_touched"] = True
    print(f"\nEnergy gained! Current energy: {room['energy']}/30")


def solve_puzzle(room):
    """Solve the symbol puzzle and award energy for success."""
    if room["puzzle_solved"]:
        print("\nYou have already solved the symbol puzzle.")
        return True

    symbols = {
        "1": "moon",
        "2": "star",
        "3": "sun",
    }

    print("\n========== THE SYMBOL PUZZLE ==========")
    print("Three symbols appear on the floor:")
    print("1. Moon")
    print("2. Star")
    print("3. Sun")
    print("\nRiddle: Which symbol represents the source")
    print("of daylight in this puzzle?")
    print("You have three attempts.")

    for attempt in range(1, 4):
        answer = ask_choice(
            f"\nAttempt {attempt}/3 — Choose 1, 2 or 3: ",
            ["1", "2", "3"],
        )

        if symbols[answer] == "sun":
            print("\nCorrect! The Sun symbol shines brightly.")
            print("The Dark Sun releases a burst of energy.")

            room["puzzle_solved"] = True
            room["attempts"] += attempt
            room["energy"] = min(30, room["energy"] + 15)

            print(f"Energy collected: {room['energy']}/30")
            return True

        print("\nIncorrect. The symbol fades.")
        room["attempts"] += 1

        if attempt == 1:
            print("Hint: Think about what gives the world daylight.")
        elif attempt == 2:
            print("Final hint: Look at the name of this room's mystery.")

    print("\nThe symbols disappear temporarily.")
    print("You can return later and try again.")
    return False


def claim_reward(state, room):
    """Award the item once and record completion."""
    if not room["puzzle_solved"]:
        print("\nSolve the puzzle before claiming the reward.")
        return

    if room["reward_claimed"]:
        print("\nYou have already collected the Dark Sun Buff.")
        return

    print("\n========== BONUS UNLOCKED ==========")
    print("You receive the Dark Sun Buff!")
    print("Your inventory has been updated.")

    if "Dark Sun Buff" not in state["inventory"]:
        state["inventory"].append("Dark Sun Buff")

    room["reward_claimed"] = True
    state["completed"]["break_room"] = True

    print("Reward: Dark Sun Buff")
    print("====================================")


def show_inventory(state):
    """Display the shared game inventory."""
    print("\n========== INVENTORY ==========")

    if not state["inventory"]:
        print("Your inventory is empty.")
    else:
        for item in state["inventory"]:
            print(f"- {item}")

    print("===============================")


def leave_room(state, room):
    """Return the player to the corridor."""
    print("\nThe Dark Sun slowly fades.")
    print("The room becomes dark again.")

    if room["reward_claimed"]:
        print("You leave with the Dark Sun Buff.")
    elif room["puzzle_solved"]:
        print("You can collect your reward before leaving next time.")
    else:
        print("The mystery remains unsolved.")

    print("\nThe adventure continues...")
    return "corridor"


def enterBreakRoom(state):
    """Main entry point for The Dark Night."""
    room = get_room_state(state)

    print("\n===================================")
    print("           THE DARK NIGHT")
    print("===================================")
    print("A strange purple light illuminates the room.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Interact with the Dark Sun")
        print("2. Solve the symbol puzzle")
        print("3. Check the Dark Sun's status")
        print("4. View inventory")
        print("5. Claim reward")
        print("6. Leave the room")

        choice = ask_choice("Choose an option: ", ["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            interact_with_sun(room)

        elif choice == "2":
            solve_puzzle(room)

        elif choice == "3":
            show_status(room)

        elif choice == "4":
            show_inventory(state)

        elif choice == "5":
            claim_reward(state, room)

        elif choice == "6":
            return leave_room(state, room)
