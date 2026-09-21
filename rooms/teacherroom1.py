import sys

def enterteacherroom1(state):
    print('\nYou stepped inside the teacher room 1\n'
            'This room seems like a mess')

    def handle_look():
        print('\nYou see a ghostly figure in the middle of the room\n'
              'It might be the teacher of this room\n'
              'Books are scattered on the floor\n'
              'And some stuff on a table'
              )

    def check_table():
        print('\nThere is a playing card on the table\n'
              'Might be tempted to take it,\n'
              'but the ghost is staring at you\n'
              'Maybe you should talk to it')


    def handle_interact():
        if not 'playing card' in state['inventory']:
            while True:
                try:
                    print('\nwelcome to my classroom\n'
                          'First thing first\n'
                          'What is 9 plus 10?\n'
                          )
                    joke_answer=int(input('Enter your answer: '))
                    if joke_answer==21:
                        print('\nHahaha!\n'
                            'I see that youre a gen z\n'
                            'Do you want this playing card?')
                        while True:
                            playing_card_to_take=input('Answer yes or no: ')
                            if playing_card_to_take=='yes':
                                state['inventory'].append('playing card')
                                state["room_states"]["classroom2031"]["playing cards"] = True
                                print('\nYou received new item in inventory!')
                                break
                            elif playing_card_to_take=='no':
                                print('\n its youre loss')
                                break
                            else:
                                print('\nIts either yes or no -_-')
                        break
                    elif joke_answer == 19:
                            print('\nThats the correct answer!\n'
                              'youre very smart')
                            break
                    elif joke_answer!=(21,19):
                        print('\nThat is not the correct answer!')
                except ValueError:
                    print('\nPlease use only numbers')
        else:
            print('\nYou already received your playing card\n'
                  'Go explore the other rooms')

    def handle_help():
        print("\nAvailable commands:")
        print("-check table          : Check whats on the table")
        print("-talk with ghost      : Interact with the ghost")
        print("- look around         : Examine the room and its contents.")
        print("- go corridor / back  : Leave the room and return to the corridor.")
        print("- ?                   : Show this help message.")
        print("- quit                : Quit the game entirely.")
        print(f' invetory: {state['inventory']}')

    def handle_go(destination):
        """Handle movement to another room."""
        if destination in ["corridor", "back"]:
            print("You leave the teacher room 1 and head back into the corridor.")
            state["previous_room"] = "teacherroom1"
            return "corridor"
        else:
            print(f"❌ You can't go to '{destination}' from here.")
            return None

    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == 'check table':
            check_table()

        elif command == "talk with ghost":
            handle_interact()

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("👋 You sit back in the softest chair, close your eyes, and exit the adventure. Game over.")
            sys.exit()

        else:
            print("❓ Unknown command. Type '?' to see available commands.")