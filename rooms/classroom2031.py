# -----------------------------------------------------------------------------
# File: classroom2031.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: September 2026
# -----------------------------------------------------------------------------

import sys
from operator import truediv
import random
import time
from data import MANIFEST

def enterClassroom2031(state):

    print("\nYou step into Classroom 2.031.")
    if state["visited"]["classroom2031"] is False:
        print("\nSuddenly a dark figure appear in front of you for a second and instantly disappeared")
        if state["room_states"]["classroom2035"]["crucifix"] is True:
            print("Crucifix start to burn and it fells out of your inventory to a ground")
            state["inventory"].remove("crucifix")
            print("Crucifix protected you from taking damage")
        elif state["room_states"]["classroom2035"]["crucifix"] is False:
            print("You have taken 4 harts of damage")
            state["health"] -= 4
            print(f"\n- Your current health is {state["health"]} harts")
        ghost = random.choice(list(MANIFEST.keys()))
        state["room_states"]["classroom2031"][MANIFEST[ghost]["item1"]] = True
        state["room_states"]["classroom2031"][MANIFEST[ghost]["item2"]] = True
        state["room_states"]["classroom2031"][MANIFEST[ghost]["item3"]] = True
        print(ghost)
    state["visited"]["classroom20314"] = True

    # --- Helperfuncties voor commandoverwerking ---

    def handle_look():
        print("\nYou take a careful look around the room.")
        print("The classroom is in a dark, you can barely see anything")
        print("In front of you on a ground is a pentagram created out of blood.")
        print("- Possible exits: nscorridor")
        state["looked_around"]["classroom2031"] = True

    def handle_help():
        print("\nAvailable commands:")
        if state["room_states"]["classroom2035"]["manifest"] is True:
            print("- manifest            : Check the manifest")
        print("- put (item)          : Put item into a pentagram")
        print("- use ouija board     : Use ouija board to speak with ghost.")
        print("--------------------------------------------------")
        print("- look around         : Examine the room and its contents.")
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")
        print(f"\n- Your current health is {state["health"]} harts")
        print("- Your current inventory:", state["inventory"])


    def handle_go(destination):
        if destination in ["corridor", "back"]:
            print("You open the door and step back into the nscorridor.")
            return "nscorridor"
        else:
            print(f"You can't go to '{destination}' from here.")
            return None

    def handle_manifest():
        print("\nManifest:")
        for i in MANIFEST:
            print(f"- name: {i}     gender: {MANIFEST[i]["gender"]}     age: {MANIFEST[i]["age"]}     favourite items: {MANIFEST[i]["item1"]}, {MANIFEST[i]["item2"]}, {MANIFEST[i]["item3"]}")
        print("\n To guess the ghost you need to tipe: are you (name)")

    def handle_ouija_board():
        if state["room_states"]["classroom2035"]["desk"] is False:
            print("you don't have ouija board")
        else:
            print("You take ouija board from your inventory")
            print("You step towards the pentagram.")
            print("\n----Ouija board questions----")
            print(" - what is your gender?")
            print(" - how old are you?")
            print(" - are you (name)?")
            question = input("\n- What do you want to ask: ")
            if question == f"are you {ghost}?":
                print("The ghost appear in front of you inside of the pentagram.")
                print("The ghost starts glowing")
                print("The ghost will change into keyshard4")
                state["inventory"].append("key shard 4") #need to add connection to lab2001
                print("- Your current inventory:", state["inventory"])
                print("\n Congratulation you have finished horror section, a new rift as appear close to a lab2001")
                state["room_states"]["classroom2031"]["ghost discovered"] = True
            elif question == "how old are you?":
                ghost_age = str(MANIFEST[ghost]["age"])
                for i in ghost_age:
                    time.sleep(1)
                    print(i)
            elif question == "what is your gender?":
                ghost_gender = MANIFEST[ghost]["gender"]
                for i in ghost_gender:
                    time.sleep(1)
                    print(i)

    def handle_put(item):
        if item == "playing cards":
            if state["room_states"]["classroom2031"]["playing cards"] is True:
                print("You put playing cards inside of the pentagram.")
                time.sleep(1)
                print("the cards starts to sort in the air")
                print("\n- playing cards are ghost's favourite item")
            else:
                print("You put playing cards inside of the pentagram.")
                time.sleep(1)
                print("nothing happen")
            state["inventory"].remove(item)
        elif item == "dog picture":
            if state["room_states"]["classroom2031"]["dog picture"] is True:
                print("You put dog picture inside of the pentagram.")
                time.sleep(1)
                print("the dog picture starts to levitate in the air and you hear ghost crying")
                print("\n- dog picture is ghost's favourite item")
            else:
                print("You put dog picture inside of the pentagram.")
                time.sleep(1)
                print("nothing happen")
            state["inventory"].remove(item)
        elif item == "photo camera":
            if state["room_states"]["classroom2031"]["photo camera"] is True:
                print("You put photo camera inside of the pentagram.")
                time.sleep(1)
                print("The photo camera takes a picture")
                print("\n- photo camera is ghost's favourite items")
            else:
                print("You put photo camera inside of the pentagram.")
                time.sleep(1)
                print("nothing happen")
            state["inventory"].remove(item)
        elif item == "football":
            if state["room_states"]["classroom2031"]["football"] is True:
                print("You put football inside of the pentagram.")
                time.sleep(1)
                print("the football flights across the room")
                print("\n- football is ghost's favourite items")
            else:
                print("You put football inside of the pentagram.")
                time.sleep(1)
                print("nothing happen")
            state["inventory"].remove(item)
        elif item == "notebook":
            if state["room_states"]["classroom2031"]["notebook"] is True:
                print("You put notebook inside of the pentagram.")
                time.sleep(1)
                print("On the notebook starts to appear some text")
                print("\n- notebook is ghost's favourite items")
            else:
                print("You put notebook inside of the pentagram.")
                time.sleep(1)
                print("nothing happen")
            state["inventory"].remove(item)
        elif item == "make-up":
            if state["room_states"]["classroom2031"]["make-up"] is True:
                print("You put make-up inside of the pentagram.")
                time.sleep(1)
                print("the make-up starts to flow in the air")
                print("\n- make-up is ghost's favourite items")
            else:
                print("You put make-up inside of the pentagram.")
                time.sleep(1)
                print("nothing happen")
            state["inventory"].remove(item)
        else:
            print("Unknown item")

    # --- Commandoloop ---
    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "?":
            handle_help()

        elif command == "manifest":
            handle_manifest()

        elif command == "use ouija board":
            handle_ouija_board()

        elif command.startswith("put "):
            if state["room_states"]["classroom2031"]["ghost discovered"] is False:
                item = command[4:].strip()
                handle_put(item)
            elif state["room_states"]["classroom2031"]["ghost discovered"] is True:
                print("The ghost was discovered in the room.")

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        else:
            print("Unknown command. Type '?' to see available commands.")