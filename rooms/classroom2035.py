# -----------------------------------------------------------------------------
# File: classroom2035.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

import sys
from .utils import chooseNextRoom
import random

def enterClassroom2035(state):

    print("\nYou step into Classroom 2.035.")
    if state["visited"]["classroom2035"] is False:
        print("The classroom is full of dust and the air is stuffy")
    state["visited"]["classroom2035"] = True

    # --- Helperfuncties voor commandoverwerking ---

    def handle_look():
        print("\nYou scan a room.")
        if state["room_states"]["classroom2035"]["folder"] is False:
            print("You can see that, on a teachers desk lies a folder.")
        if state["room_states"]["classroom2035"]["football"] is False:
            print("In the corner of the room is a football.")
        if state["room_states"]["classroom2035"]["board"] is False:
            print("On a board is unfinished game of hangman.")
        if state["room_states"]["classroom2035"]["desk"] is False:
            print("On a desk in the back of the room lies something but you can't see what it is.")
        if state["room_states"]["classroom2035"]["folder"] is True and state["room_states"]["classroom2035"]["board"] is True and state["room_states"]["classroom2035"]["desk"] is True and state["room_states"]["classroom2035"]["football"] is True:
            print("There is nothing more you can do")
        print("- Possible exits: nscorridor")
        state["looked_around"]["classroom2035"] = True


    def handle_help():
        print("\nAvailable commands:")
        if state["room_states"]["classroom2035"]["manifest"] is True:
            print("- manifest            : Check the manifest")
        if state["room_states"]["classroom2035"]["folder"] is False or state["room_states"]["classroom2035"]["desk"] is False or state["room_states"]["classroom2035"]["board"] is False or state["room_states"]["classroom2035"]["football"] is False:
            print("- investigate         : Check some areas of the room")
            if state["room_states"]["classroom2035"]["folder"] is False:
                print("      ‣ folder        : Check the folder on a teachers desk")
            if state["room_states"]["classroom2035"]["desk"] is False:
                print("      ‣ desk          : Check the student desk in the back")
            if state["room_states"]["classroom2035"]["board"] is False:
                print("      ‣ board         : Check the board")
            if state["room_states"]["classroom2035"]["football"] is False:
                print("      ‣ football      : Check the football")
        if state["room_states"]["classroom2035"]["folder"] is False or state["room_states"]["classroom2035"]["desk"] is False or state["room_states"]["classroom2035"]["board"] is False or state["room_states"]["classroom2035"]["football"] is False or state["room_states"]["classroom2035"]["manifest"] is True:
            print("--------------------------------------------------")
        print("- look around         : Examine the room and its contents.")
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")
        print(f"\n- Your current health is {state["health"]} harts")
        print("- Your current inventory:", state["inventory"])

    def handle_investigate(item):
        if item == "folder":
            if state["room_states"]["classroom2035"]["folder"] is True:
                print("There is no other folder on a desk.")
            else:
                print("You go closer to a teachers desk.")
                print("You pick up the file and open the file.")
                print("A kay falls out of the file and you pick it up.")
                print("It's a key from the Classroom2031.")
                print("Inside is a manifest with name of the students their ages and 3 of their favourite items.")
                print("Also there is a note 'To exit this place you need to guess the ghost'")
                print("You pick up manifest and key2031 to your inventory.")
                state["inventory"].append("manifest")
                state["room_states"]["classroom2035"]["manifest"] = True
                state["inventory"].append("key2031")
                print("\n- Your current inventory:", state["inventory"])
                state["room_states"]["classroom2035"]["folder"] = True

        elif item == "desk":
            if state["room_states"]["classroom2035"]["desk"] is True:
                print("There is nothing on a desk")
            else:
                print("You go closer to a desk in a back of the room")
                print("You can see its an ouija board for communicating with ghosts")
                print("You pick up ouija board and store in your inventory")
                state["inventory"].append("ouija board")
                print("- Your current inventory:", state["inventory"])
                state["room_states"]["classroom2035"]["desk"] = True

        elif item == "board":
            if state["room_states"]["classroom2035"]["board"] is True:
                print("The hangman is solved there is nothing else to do")
            else:
                print("You step to the board and you can see there is unfinished game of hangman.")
                print("You take marker into your hand and try to guess the word")
                print("You can only guess one letter at a time, based on that hangman will appear")
                wanna_play = input("Wanna play? (y/n): ").lower()
                if wanna_play == "y" or wanna_play == "yes":
                    handle_hangman()
                elif wanna_play == "n" or wanna_play == "no":
                    print("You put the marker back and step back to the door.")
                else:
                    print("unknown command")

        elif item == "football":
            if state["room_states"]["classroom2035"]["football"] is True:
                print("You have the football in your inventory")
            else:
                print("You go to the corner of the room and check the ball.")
                print("Its a normal football, you will pick it up to your inventory")
                state["inventory"].append("football")
                print("- Your current inventory:", state["inventory"])
                state["room_states"]["classroom2035"]["football"] = True

        else:
            print(f"There is no '{item}' here to investigate.")

    def handle_hangman():
        word = random.choice(state["hangman_words"])
        word_letters = []
        for i in word:
            word_letters.append(i)
        print(word_letters)
        while state["room_states"]["classroom2035"]["game_over"] is not True:
            print("---------------------------------------------")
            print("▒█░▒█ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█")
            print("▒█▀▀█ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█")
            print("▒█░▒█ ▒█░▒█ ▒█░░▀█ ▒█▄▄█ ▒█░░▒█ ▒█░▒█ ▒█░░▀█")
            print("---------------------------------------------")
            print("_______")
            print("|     |")
            if state["room_states"]["classroom2035"]["wrong_guess"] >= 1:
                print("|     O")
            else:
                print("|      ")
            if state["room_states"]["classroom2035"]["wrong_guess"] >= 4:
                print("|    /|\\")
            elif state["room_states"]["classroom2035"]["wrong_guess"] >= 3:
                print("|    /|")
            elif state["room_states"]["classroom2035"]["wrong_guess"] >= 2:
                print("|     |")
            else:
                print("|     ")
            if state["room_states"]["classroom2035"]["wrong_guess"] >= 6:
                print("|    / \\")
            elif state["room_states"]["classroom2035"]["wrong_guess"] >= 5:
                print("|    / ")
            else:
                print("|     ")
            print("---------------------------------------------")
            unraveled_word = ""
            for i in word:
                if i in state["room_states"]["classroom2035"]["guessed_letters"]:
                    unraveled_word += i
                else:
                    unraveled_word += "_"

            print(f"\nWord: {unraveled_word}")
            if unraveled_word == word and state["room_states"]["classroom2035"]["wrong_guess"] <= 6:
                print("\nYou win!")
                print("\nYou hear opening of the box behind you.")
                print("You turn around and look inside the box")
                print("There is a crucifix inside the box, you take the crucifix")
                state["inventory"].append("crucifix")
                state["room_states"]["classroom2035"]["crucifix"] = True
                print("- Your current inventory:", state["inventory"])
                state["room_states"]["classroom2035"]["game_over"] = True
                state["room_states"]["classroom2035"]["board"] = True
            elif unraveled_word != word and state["room_states"]["classroom2035"]["wrong_guess"] >= 6:
                print("\nYou lose!")
                print("\nYou lost a chance to win the game.")
                state["room_states"]["classroom2035"]["game_over"] = True
                state["room_states"]["classroom2035"]["board"] = True
            else:
                letter = input("Guess a letter: ")
                state["room_states"]["classroom2035"]["guessed_letters"].append(letter)
                if letter not in word_letters:
                    state["room_states"]["classroom2035"]["wrong_guess"] += 1

    def handle_manifest():
        print("\nManifest:")
        for i in state["manifest"]:
            print(f"- name: {i}     gender: {state["manifest"][i]["gender"]}     age: {state["manifest"][i]["age"]}     favourite items: {state["manifest"][i]["item1"]}, {state["manifest"][i]["item2"]}, {state["manifest"][i]["item3"]}")
        print("\n To guess the ghost you need to tipe: are you (name)")

    def handle_go(destination):
        if destination in ["nscorridor", "back"]:
            print("You open the door and step back into the nscorridor.")
            state["previous_room"] = "classroom2035"
            return "nscorridor"
        else:
            print(f"You can't go to '{destination}' from here.")
            return None

    # --- Commandoloop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command.startswith("investigate"):
            item = command[12:].strip()
            handle_investigate(item)

        elif command == "manifest":
            handle_manifest()

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("👋 You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")