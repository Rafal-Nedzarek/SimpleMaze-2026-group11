import sys
from functions import shared_functions as sf
from .utils import debugMode, healing

from data import examroom_texts
def enterexamroom(state):
    examroom_texts.welcome_screen()

    def answers_check(answers):
        correct_answers = ['A', 'B', 'C', 'D']
        correct=0
        for key, ans in zip(correct_answers,answers):
            if key==ans:
                correct+=1
        return correct


    def interact_teacher():
        if 'crooked key' not in state['inventory']:
            print('Hallo! Are you ready for your history exam?')
            respond=input('Enter yes or no\n'
                          'Enter: ')
            while True:
                if respond=='no':
                    print('Come back when you are ready for the test!')
                    break
                elif respond=='yes':
                    print()
                    examroom_texts.questions_sheet()
                    answers = input('answer: ').upper().split(",")
                    print(answers)
                    result=answers_check(answers)
                    if result==4:
                        print('congratulation! You passed the exam\n'
                              'Here is the key for teacherroom1')
                        state['inventory'].append('crooked key')
                        break
                    else:
                        print('unfortunately you did not passed the test\n'
                              'Better luck next time!')
                        break

                else:
                    print('its yes or no')
        else:
            print('You already passed the exam')

    def interact_book():
        print('There is a book with title: Exam')
        respond=input('Would you like to look inside the book?')
        while respond!=('yes'):
            break
        if respond=='yes':
            examroom_texts.questions_answers()


    def handle_help():
        print("\nAvailable commands:")
        print("- talk with teacher   : interact with the teacher")
        print("- book                : Examine the book")
        if state["health"]<10 and state["inventory"] == "bandages" :
            print("- use bandages        : Use bandages to heal 4 harts.")
        print("--------------------------------------------------")
        sf.show_universal_help_text()
        print(f' invetory: {state['inventory']}')

    def handle_go(destination):
        if destination in ["corridor", "back"]:
            print("You leave the examroom and head back into the corridor.")
            state["previous_room"] = "examroom"
            return "corridor"
        else:
            print(f"You can't go to '{destination}' from here.")
            return None

    def handle_look():
        print('You see a teacher sitting on his desk\n'
              'Bookshelves with interesting books\n')


    while True:
        command = input("\n> ").strip().lower()

        if command == "look around":
            handle_look()

        elif command == "talk with teacher":
            interact_teacher()

        elif command == "book":
            interact_book()

        elif command == "?":
            handle_help()

        elif command.startswith("go "):
            destination = command[3:].strip()
            result = handle_go(destination)
            if result:
                return result

        elif command == "quit":
            print("You sit back in the softest chair, close your eyes, and exit the adventure. Game over.")
            sys.exit()

        else:
            print("Unknown command. Type '?' to see available commands.")
