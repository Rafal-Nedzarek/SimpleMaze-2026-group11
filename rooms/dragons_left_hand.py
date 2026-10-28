
def get_room_state(state):
    """Initialize and retrieve persistent room progress."""
    state.setdefault("inventory", [])
    state.setdefault("completed", {})
    state.setdefault("room_states", {})

    return state["room_states"].setdefault(
        "dragons_left_hand",
        {
            "trial1": False,
            "trial2": False,
            "trial3": False,
            "reward_claimed": False,
        },
    )


def ask_answer(prompt, correct_answer, wrong_message, hint=None):
    """Repeat a trial until the correct answer is given."""
    while True:
        answer = input(prompt).strip().lower()

        if answer == correct_answer:
            print("\nCorrect!")
            return True

        print("\nWRONG!")
        print(wrong_message)

        if hint:
            print(hint)


def trial_dragon_coins(room):
    """Trial 1: calculate the total number of coins."""
    if room["trial1"]:
        print("\nTrial 1 is already completed. Number: 36")
        return

    print("\n==============================================")
    print("                  TRIAL 1")
    print("==============================================")
    print("\nThe knight puts some gold coins on a table.")
    print('"There are 3 bags."')
    print('"Each bag contains 12 coins."')
    print('"I take 5 coins from the first bag and move')
    print('them into the second bag."')
    print("\nHow many coins are there in total?")
    print("Moving coins does not change the total.")

    ask_answer(
        "\nYour answer: ",
        "36",
        "The knight laughs.",
        "You moved the coins, but you did not destroy them.",
    )

    room["trial1"] = True
    print("\nThe number 36 appears on the wall.")


def trial_three_buttons(room):
    """Trial 2: identify the only button satisfying both clues."""
    if room["trial2"]:
        print("\nTrial 2 is already completed. Number: 7")
        return

    print("\n==============================================")
    print("                  TRIAL 2")
    print("==============================================")
    print("\nYou see three buttons.")
    print("1. RED")
    print("2. BLUE")
    print("3. GOLD")
    print('\n"The correct button is NOT red."')
    print('"The correct button is NOT gold."')

    while True:
        answer = input("\nChoose 1, 2 or 3: ").strip()

        if answer == "2":
            break
        elif answer == "1":
            print("\nWRONG BUTTON! The red button makes a loud noise.")
        elif answer == "3":
            print("\nWRONG BUTTON! The gold button releases water.")
        else:
            print("\nThat button does not exist.")

        print("The buttons reset. Try again.")

    print("\nYou press the BLUE button.")
    print("CLICK!")
    print("Nothing explodes. You are relieved.")

    room["trial2"] = True
    print("\nThe number 7 appears on the wall.")


def trial_stone_sequence(room):
    """Trial 3: solve the number sequence."""
    if room["trial3"]:
        print("\nTrial 3 is already completed. Number: 30")
        return

    print("\n==============================================")
    print("                  TRIAL 3")
    print("==============================================")
    print("\nFour numbers appear on a stone tablet.")
    print("2")
    print("6")
    print("12")
    print("20")
    print("?")
    print('\n"There is a simple mathematical rule."')

    ask_answer(
        "\nYour answer: ",
        "30",
        "The stone tablet becomes darker.",
        "Look at the differences between consecutive numbers.",
    )

    room["trial3"] = True
    print("\nThe stone tablet glows.")
    print("The number 30 appears on the wall.")


def show_final_code(room):
    """Display the numbers once all three trials are complete."""
    if not all(room[key] for key in ("trial1", "trial2", "trial3")):
        print("\nThe final code is still locked.")
        print("You must complete all three trials first.")
        return False

    print("\n==============================================")
    print("                THE FINAL CODE")
    print("==============================================")
    print("\nFirst: 36")
    print("Second: 7")
    print("Third: 30")
    print('\n"The numbers are the key."')
    print('"Put them together in the order you found them."')
    return True


def claim_key_shard(state, room):
    """Award the Key Shard only once."""
    if room["reward_claimed"]:
        print("\nYou already have the Key Shard.")
        return

    print("\n==============================================")
    print("                 KEY SHARD")
    print("==============================================")
    print("\nYou received: KEY SHARD")

    if "Key Shard" not in state["inventory"]:
        state["inventory"].append("Key Shard")

    room["reward_claimed"] = True
    state["completed"]["dragons_left_hand"] = True

    print('\nThe knight says:')
    print('"This is one piece of a larger key."')
    print('"You will need it later."')
    print("\nThe Key Shard begins to glow.")
    print("A strange symbol appears inside it, then disappears.")


def show_inventory(state):
    """Show the game's shared inventory."""
    print("\n========== INVENTORY ==========")

    if not state["inventory"]:
        print("Your inventory is empty.")
    else:
        for item in state["inventory"]:
            print(f"- {item}")

    print("===============================")


def enterDragonsLeftHand(state):
    """Main entry point for The Dragon's Left Hand."""
    room = get_room_state(state)

    print("\n==============================================")
    print("          THE DRAGON'S LEFT HAND")
    print("==============================================")
    print("\nYou enter a large dark chamber.")
    print("A knight wearing black dragon armor stands before you.")
    print('\n"I am the Dragon\'s Left Hand."')
    print('"If you want the Key Shard, pass my trials."')

    while True:
        print("\nWhat would you like to do?")
        print("1. Trial 1 - The Dragon Coins")
        print("2. Trial 2 - The Three Buttons")
        print("3. Trial 3 - The Stone Sequence")
        print("4. View the final code")
        print("5. Check inventory")
        print("6. Leave the chamber")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            trial_dragon_coins(room)

        elif choice == "2":
            trial_three_buttons(room)

        elif choice == "3":
            trial_stone_sequence(room)

        elif choice == "4":
            if not show_final_code(room):
                continue

            if room["reward_claimed"]:
                print("\nYou have already claimed the Key Shard.")
                continue

            code = input("\nEnter the final code: ").strip()

            if code == "36730":
                print("\n==============================================")
                print("                CODE ACCEPTED!")
                print("==============================================")
                print("\nThe entire chamber begins to shake.")
                print("CLANG... CLANG... CLANG...")
                print("\nThe knight opens his armored hand.")
                print("A small golden object appears.")
                claim_key_shard(state, room)
            else:
                print("\nWRONG CODE! The knight looks disappointed.")

        elif choice == "5":
            show_inventory(state)

        elif choice == "6":
            print("\nThe knight steps aside.")
            print('"Your journey is not over."')
            print("\nYou leave the chamber.")
            return "corridor"

        else:
            print("\nInvalid choice. Choose a number from 1 to 6.")
