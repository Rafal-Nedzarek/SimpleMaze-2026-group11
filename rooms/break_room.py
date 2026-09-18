
def enterBreakRoom(state):
    print("===================================")
    print("          THE DARK NIGHT")
    print("===================================")

    print("\nYou enter a strange dark room.")
    print("There is almost no light.")
    print("You look around and see nothing...")
    print("Suddenly, a small Dark Sun appears above you.")
    print("It is glowing with a strange purple light.")

    answer = input("\nDo you want to touch the Dark Sun? (yes/no): ")

    while answer != "yes" and answer != "no":
        print("\nThe Dark Sun does not understand you.")
        print("Please answer with yes or no.")
        answer = input("\nDo you want to touch the Dark Sun? (yes/no): ")

    if answer == "yes":
        print("\nYou slowly touch the Dark Sun...")
        print("BOOM!")
        print("The whole room becomes bright for a few seconds.")
        print("You feel a strange power inside your body.")

    else:
        print("\nYou decide not to touch the Dark Sun.")
        print("You take one step back...")
        print("The Dark Sun becomes brighter.")
        print("You take another step back...")
        print("It becomes even brighter.")
        print("\nYou realize that the Dark Sun does not care about your answer.")
        print("It gives you the power anyway.")

    print("\nSuddenly, three symbols appear on the floor.")
    print("A moon, a star and a sun.")
    print("A message appears:")
    print('"Only one of these gives light during the day."')

    puzzle = input("\nWhich symbol is the answer? (moon/star/sun): ")

    while puzzle != "sun":
        print("\nWrong answer!")
        print("The Dark Sun is disappointed.")
        print("It becomes 1% darker...")
        print("You probably should try again.")

        puzzle = input("\nTry again. Which symbol is the answer? (moon/star/sun): ")

    print("\nCorrect!")
    print("The Dark Sun suddenly becomes extremely bright.")
    print("You hear a mysterious sound...")
    print("PFFFFT!")

    print("Nothing happens.")
    print("Apparently, the Dark Sun just sneezed.")

    print("\nBONUS UNLOCKED!")
    print("Dark Sun Buff: +10% extra energy.")

    state["inventory"].append("Dark Sun Buff")

    print("\n-----------------------------------")
    print("Your inventory:")
    print(state["inventory"])
    print("-----------------------------------")

    leave = input("\nDo you want to leave the Dark Night? (yes/no): ")

    while leave != "yes" and leave != "no":
        print("\nPlease answer with yes or no.")
        leave = input("\nDo you want to leave the Dark Night? (yes/no): ")

    if leave == "no":
        print("\nYou decide to stay for a little longer.")
        print("You look at the Dark Sun...")
        print("The Dark Sun looks back.")
        print("This is getting awkward...")

        leave = input("\nNow, do you want to leave the Dark Night? (yes/no): ")

        while leave != "yes":
            print("\nThe adventure must continue.")
            print("There is nothing else to do here.")
            leave = input("\nDo you want to leave the Dark Night? (yes/no): ")

    print("\nYou leave the Dark Night.")
    print("The Dark Sun slowly disappears.")
    print("The room becomes dark again.")

    print("\n===================================")
    print("          ROOM COMPLETED!")
    print("===================================")
    print("You completed The Dark Night.")
    print("You received the Dark Sun Buff.")
    print("The adventure continues in another room.")
    print("===================================")
    return "corridor"