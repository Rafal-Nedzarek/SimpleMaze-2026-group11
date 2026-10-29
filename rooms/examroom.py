import sys
from functions import shared_functions as sf
from .utils import debugMode

from data import examroom_texts
def enterexamroom(state):
    examroom_texts.welcome_screen()
    state["visited"]["examroom"] = True

    def answers_check(answers):
        cleaned_answers=[]

        for letter in answers:
            cleaned_answers.append(letter.upper())
        correct_answers = ['A', 'B', 'C', 'D']
        correct=0
        for key, ans in zip(correct_answers,cleaned_answers):
            if key==ans:
                correct+=1
        return correct


    def interact_teacher():
        if 'crooked key' not in state['inventory']:
            print('Hallo! Are you ready for your history exam?')
            while True:
                respond = input('Enter yes or no\n'
                                'Enter: ')
                r=respond.lower()
                if r=='no':
                    print('Come back when you are ready for the test!')
                    break
                elif r=='yes':
                    examroom_texts.questions_sheet()
                    answers =input('answer: ').strip().upper().split(",")
                    result=answers_check(answers)
                    if result==4:
                        print('congratulation! You passed the exam\n'
                              'Here is the key for teacherroom1')
                        state['inventory'].append('crooked key')
                        state['completed']['examroom'] = True
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
        respond = input('Would you like to look inside the book?')
        while respond!='yes' and respond!='no':
            print('\nPlease answer with yes or no')
            respond = input('Would you like to look inside the book?')
        if respond=='yes':
            examroom_texts.questions_answers()
        else:
            print("You've put the book back into the bookshelve")


    def handle_help():
        print("\nAvailable commands:")
        print("- talk with teacher   : interact with the teacher")
        print("- book                : Examine the book")
        if state["health"]<10 and state["inventory"] == "bandages" :
            print("- use bandages        : Use bandages to heal 4 harts.")
        print("--------------------------------------------------")
        sf.show_universal_help_text()

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

        elif command == "status":
            sf.show_completion(state["completed"],state)

        elif command == "quit":
            print("You sit back in the softest chair, close your eyes, and exit the adventure. Game over.")
            sys.exit()
        elif command == "map":
            sf.display_map(state)

        elif command == "pause":
            sf.write_save_file(state["user_name"], state)
            sys.exit()

        elif command == "scoreboard":
            sf.display_leaderboard()

        else:
            print("Unknown command. Type '?' to see available commands.")


