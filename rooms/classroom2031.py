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
from functions import shared_functions as sf


def enterClassroom2031(state):

    print("\nYou step into Classroom 2.031.")
    if state["visited"]["classroom2031"] is False:
        print("\nSuddenly a dark figure appears in front of you for a second and instantly disappears")
        if state["room_states"]["classroom2035"]["crucifix"] is True:
            print("The crucifix starts to burn and falls to the ground.")
            state["inventory"].remove("crucifix")
            print("The crucifix protected you from taking damage")
        elif state["room_states"]["classroom2035"]["crucifix"] is False:
            print("You have taken 4 harts of damage")
            state["health"] -= 4
            print(f"\n- Your current health is {state["health"]} harts")
        ghost = random.choice(list(MANIFEST.keys()))
        state["room_states"]["classroom2031"][MANIFEST[ghost]["item1"]] = True
        state["room_states"]["classroom2031"][MANIFEST[ghost]["item2"]] = True
        state["room_states"]["classroom2031"][MANIFEST[ghost]["item3"]] = True
    state["visited"]["classroom2031"] = True

    # --- Helperfuncties voor commandoverwerking ---

    def handle_look():
        print("\nYou take a careful look around the room.")
        print("The classroom is dark, you can barely see anything")
        print("In front of you on the ground is a pentagram created out of blood.")
        print("- Possible exits: nscorridor")
        state["looked_around"]["classroom2031"] = True

    def handle_help():
        print("\nAvailable commands:")
        if state["room_states"]["classroom2035"]["manifest"] is True:
            print("- manifest            : Check the manifest")
        if state["room_states"]["classroom2031"]["playing cards"] is True or state["room_states"]["classroom2031"]["dog picture"] is True or state["room_states"]["classroom2031"]["photo camera"] is True or state["room_states"]["classroom2031"]["football"] is True or state["room_states"]["classroom2031"]["notebook"] is True or state["room_states"]["classroom2031"]["make-up"] is True:
            print("- put                 : Put item into a pentagram")
            if state["room_states"]["classroom2031"]["playing cards"] is True:
                print("      ‣ playing cards   : Put playing cards in the pentagram")
            if state["room_states"]["classroom2031"]["dog picture"] is True:
                print("      ‣ dog picture   : Put dog picture in the pentagram")
            if state["room_states"]["classroom2031"]["photo camera"] is True:
                print("      ‣ photo camera   : Put photo camera in the pentagram")
            if state["room_states"]["classroom2031"]["football"] is True:
                print("      ‣ football   : Put football in the pentagram")
            if state["room_states"]["classroom2031"]["notebook"] is True:
                print("      ‣ notebook   : Put notebook in the pentagram")
            if state["room_states"]["classroom2031"]["make-up"] is True:
                print("      ‣ make-up   : Put make-up in the pentagram")
        if state["room_states"]["classroom2035"]["desk"] is True:
            print("- use ouija board     : Use ouija board to speak with ghost.")
        if state["health"]<10 and state["inventory"] == "bandages" :
            print("- use bandages        : Use bandages to heal 4 harts.")
        if state["room_states"]["classroom2035"]["manifest"] is True:
            print("--------------------------------------------------")
        print("- use bandages        : Use bandages to heal 4 harts.")
        sf.show_universal_help_text()

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
            print("you don't have the Ouija board")
        else:
            print("You take the Ouija board from your inventory")
            print("You step towards the pentagram.")
            print("\n----Ouija board questions----")
            print(" - what is your gender?")
            print(" - how old are you?")
            print(" - are you (name)?")
            question = input("\n- What do you want to ask: ")
            if question == f"are you {ghost}?":
                print("The ghost appears in front of you inside of the pentagram.")
                print("The ghost starts glowing")
                print("The ghost will transforms into key shard 4")
                state["inventory"].append("key shard 4") #need to add connection to lab2001
                print("- Your current inventory:", state["inventory"])
                print("Congratulations! You have finished the horror section. A has opened to Lab 2.001.")
                state["room_states"]["classroom2031"]["ghost discovered"] = True
                state["room_states"]["classroom2035"]["manifest"] = False
                state["completed"]["classroom2031"] = True
                state["section_finished"]["horror"] = True
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
            else:
                print("You asked an invalid question or forgot to put ? at the end.")

    def handle_put(item):
        if item == "playing cards":
            if state["room_states"]["classroom2031"]["playing cards"] is True:
                print("You put playing cards inside of the pentagram.")
                time.sleep(1)
                print("The cards starts to sort in the air")
                print("\n- playing cards are ghost's favourite item")
            else:
                print("You put playing cards inside of the pentagram.")
                time.sleep(1)
                print("Nothing happens.")
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
                print("Nothing happens.")
            state["inventory"].remove(item)
        elif item == "photo camera":
            if state["room_states"]["classroom2031"]["photo camera"] is True:
                print("You put photo camera inside of the pentagram.")
                time.sleep(1)
                print("The photo camera takes a picture")
                print("\n- photo camera is ghost's favourite item")
            else:
                print("You put photo camera inside of the pentagram.")
                time.sleep(1)
                print("Nothing happens.")
            state["inventory"].remove(item)
        elif item == "football":
            if state["room_states"]["classroom2031"]["football"] is True:
                print("You put football inside of the pentagram.")
                time.sleep(1)
                print("The football flies across the room")
                print("\n- football is ghost's favourite item")
            else:
                print("You put football inside of the pentagram.")
                time.sleep(1)
                print("Nothing happens.")
            state["inventory"].remove(item)
        elif item == "notebook":
            if state["room_states"]["classroom2031"]["notebook"] is True:
                print("You put notebook inside of the pentagram.")
                time.sleep(1)
                print("On the notebook starts to appear some text")
                print("\n- notebook is ghost's favourite item")
            else:
                print("You put notebook inside of the pentagram.")
                time.sleep(1)
                print("Nothing happens.")
            state["inventory"].remove(item)
        elif item == "make-up":
            if state["room_states"]["classroom2031"]["make-up"] is True:
                print("You put make-up inside of the pentagram.")
                time.sleep(1)
                print("The make-up starts to float in the air")
                print("\n- make-up is ghost's favourite item")
            else:
                print("You put make-up inside of the pentagram.")
                time.sleep(1)
                print("Nothing happens.")
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

        elif command == "use bandages":
            if "bandages" in state["inventory"]:
                sf.healing(state)
            else:
                print("You don't have any bandages.")

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("You drop your backpack, leave the maze behind, and step back into the real world.")
            sys.exit()

        elif command == "status":
            sf.show_completion(state["completed"],state)

        else:
            print("Unknown command. Type '?' to see available commands.")