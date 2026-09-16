def enterEnchantedLibrary(state):
    print("======================================")
    print("       THE ENCHANTED LIBRARY")
    print("          Classroom 2.015")
    print("======================================")

    while True:

        print()
        print("You are inside the Enchanted Library.")
        print()
        print("1. Explore the left bookshelf")
        print("2. Explore the middle bookshelf")
        print("3. Explore the right bookshelf")
        print("4. Explore the old table")
        print("5. Check inventory")
        print("6. Try to open the spellbook")
        print("7. Leave the library")

        choice = input("Choose an option: ")

        # FIRST CLUE
        if choice == "1":

            print()
            print("You walk to the left bookshelf.")
            print("You find an old book called 'The Beginning of Every Story'.")
            print()
            print("Inside the book you find a message:")
            print()
            print("Every story has a beginning.")
            print("Find the page where every story starts.")
            print()

            if state["room_states"]["enchanted_library"]["clue1_solved"]:
                print("You already solved this puzzle.")

            else:
                answer = input("What page does every book start with? ")

                if answer == "1":
                    print()
                    print("Correct!")
                    print("You discovered the first number: 1")
                    state["room_states"]["enchanted_library"]["clue1_solved"] = True

                else:
                    print()
                    print("Wrong answer.")
                    print("Think about the first page of a book.")

        # SECOND CLUE
        elif choice == "2":

            print()
            print("You walk to the middle bookshelf.")
            print("You find a large book about legendary creatures.")
            print()
            print("You open the book and see a picture of a dragon.")
            print()
            print("A message underneath the picture says:")
            print()
            print("Count the legs of the creature in front of you.")
            print()

            if state["room_states"]["enchanted_library"]["clue2_solved"]:
                print("You already solved this puzzle.")

            else:
                answer = input("How many legs does the dragon have? ")

                if answer == "4":
                    print()
                    print("Correct!")
                    print("You discovered the second number: 4")
                    state["room_states"]["enchanted_library"]["clue2_solved"] = True

                else:
                    print()
                    print("Wrong answer.")
                    print("Look carefully at the dragon.")

        # THIRD CLUE
        elif choice == "3":

            print()
            print("You walk to the right bookshelf.")
            print("You find a golden book.")
            print()
            print("The word MAGIC is written on the cover.")
            print()
            print("Inside the book you find a message:")
            print()
            print("Words can hide numbers.")
            print("Count every letter in the word on the cover.")
            print()

            if state["room_states"]["enchanted_library"]["clue3_solved"]:
                print("You already solved this puzzle.")

            else:
                answer = input("How many letters are in MAGIC? ")

                if answer == "5":
                    print()
                    print("Correct!")
                    print("You discovered the third number: 5")
                    state["room_states"]["enchanted_library"]["clue3_solved"] = True

                else:
                    print()
                    print("Wrong answer.")
                    print("Count the letters in MAGIC carefully.")

        # NOTEBOOK
        elif choice == "4":

            print()
            print("You walk to the old table.")
            print("You see candles, an ancient spellbook and a Notebook.")
            print()

            if "Notebook" in state["inventory"]:
                print("You already collected the Notebook.")

            else:
                answer = input("Do you want to take the Notebook? (yes/no): ")

                if answer.lower() == "yes":
                    state["inventory"].append("Notebook")
                    print()
                    print("You picked up the Notebook.")
                    print("Maybe I will need to use it in another section or another place.")

                else:
                    print()
                    print("You leave the Notebook on the table.")

        # INVENTORY
        elif choice == "5":

            print()
            print("========== INVENTORY ==========")

            if len(state["inventory"]) == 0:
                print("Your inventory is empty.")

            else:
                for item in state["inventory"]:
                    print("- " + item)

            print("===============================")

        # SPELLBOOK
        elif choice == "6":

            print()

            if state["room_states"]["enchanted_library"]["spellbook_unlocked"]:
                print("The spellbook is already open.")

            elif state["room_states"]["enchanted_library"]["clue1_solved"] and state["room_states"]["enchanted_library"]["clue2_solved"] and state["room_states"]["enchanted_library"]["clue3_solved"]:

                print("You have discovered all three numbers.")
                print()
                print("The spellbook has a three-number lock.")
                print("Enter the numbers in the order you discovered them.")
                print()

                code = input("Enter the code: ")

                if code == "145":

                    print()
                    print("======================================")
                    print("             CORRECT!")
                    print("======================================")
                    print()
                    print("The magical lock disappears.")
                    print("The ancient spellbook opens.")
                    print()
                    print("You find a mysterious message:")
                    print()
                    print("The treasure is closer than you think.")
                    print("Seek the place where the dragon watches")
                    print("over the old tower.")
                    print()
                    print("Suddenly, something falls from the spellbook.")
                    print("It is an old golden key.")
                    print()
                    print("You picked up the Golden Key.")
                    print("The key has been added to your inventory.")
                    print()
                    print("The key may unlock the door to the")
                    print("Dragon's Chamber.")
                    print()
                    print("You have discovered an important clue")
                    print("for the next part of the adventure.")

                    state["inventory"].append("Golden Key")
                    state["room_states"]["enchanted_library"]["spellbook_unlocked"] = True

                else:
                    print()
                    print("Wrong code.")
                    print("The spellbook remains locked.")
                    print("Try again.")

            else:

                print("The spellbook is locked.")
                print()
                print("You need to solve all three puzzles first.")

                if not state["room_states"]["enchanted_library"]["clue1_solved"]:
                    print("First clue is still unsolved.")

                if not state["room_states"]["enchanted_library"]["clue2_solved"]:
                    print("Second clue is still unsolved.")

                if not state["room_states"]["enchanted_library"]["clue3_solved"]:
                    print("Third clue is still unsolved.")

        # LEAVE
        elif choice == "7":

            print()
            print("You leave Classroom 2.015.")
            print("Your inventory stays with you.")
            print()
            print("The adventure continues in another room.")
            return "corridor"

            #break

        else:

            print()
            print("Invalid option.")
            print("Please choose a number from 1 to 7.")

    print()
    print("======================================")
    print("       THE ADVENTURE CONTINUES")
    print("======================================")