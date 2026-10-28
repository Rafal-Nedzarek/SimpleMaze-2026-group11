def show_library_menu():
    print("\n=== THE ENCHANTED LIBRARY | 2.015 ===")
    print("1. Left bookshelf")
    print("2. Middle bookshelf")
    print("3. Right bookshelf")
    print("4. Old table")
    print("5. Inventory")
    print("6. Spellbook")
    print("7. Leave")


def solve_clue(state, clue_number, question, correct_answer):
    library = state["room_states"]["enchanted_library"]
    clue_key = f"clue{clue_number}_solved"

    if library[clue_key]:
        print(f"Clue {clue_number} already solved.")
        return

    answer = input(question).strip()

    if answer == correct_answer:
        library[clue_key] = True
        print(f"Correct! Number {correct_answer} found.")
    else:
        print("Wrong answer. Try again.")


def explore_left_shelf(state):
    print("\nThe Beginning of Every Story")

    solve_clue(
        state,
        1,
        "What page does every book start with? ",
        "1"
    )


def explore_middle_shelf(state):
    print("\nA book about dragons.")

    solve_clue(
        state,
        2,
        "How many legs does a dragon have? ",
        "4"
    )


def explore_right_shelf(state):
    print("\nA golden book marked MAGIC.")

    solve_clue(
        state,
        3,
        "How many letters are in MAGIC? ",
        "5"
    )


def explore_old_table(state):
    if "Notebook" in state["inventory"]:
        print("Notebook already collected.")
        return

    answer = input("Take the Notebook? (yes/no): ").strip().lower()

    if answer == "yes":
        state["inventory"].append("Notebook")
        state["room_states"]["classroom2031"]["notebook"] = True
        print("Notebook collected.")
    else:
        print("Notebook left on the table.")


def show_inventory(state):
    print("\n=== INVENTORY ===")

    if not state["inventory"]:
        print("Empty.")
        return

    for item in state["inventory"]:
        print(f"- {item}")


def open_spellbook(state):
    library = state["room_states"]["enchanted_library"]

    if library["spellbook_unlocked"]:
        print("Spellbook already open.")
        return

    clues_solved = all(
        library[f"clue{i}_solved"]
        for i in range(1, 4)
    )

    if not clues_solved:
        print("Solve all 3 clues first.")
        return

    code = input("Enter the code: ").strip()

    if code != "145":
        print("Wrong code.")
        return

    library["spellbook_unlocked"] = True

    if "Golden Key" not in state["inventory"]:
        state["inventory"].append("Golden Key")

    print("\nSpellbook opened!")
    print("Golden Key collected.")
    print("Clue: Seek the place where the dragon")
    print("watches over the old tower.")


def enterEnchantedLibrary(state):
    while True:
        show_library_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            explore_left_shelf(state)

        elif choice == "2":
            explore_middle_shelf(state)

        elif choice == "3":
            explore_right_shelf(state)

        elif choice == "4":
            explore_old_table(state)

        elif choice == "5":
            show_inventory(state)

        elif choice == "6":
            open_spellbook(state)

        elif choice == "7":
            print("Leaving the library.")
            return "corridor"

        else:
            print("Invalid option.")
