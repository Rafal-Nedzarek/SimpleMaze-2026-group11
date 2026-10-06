import time
start_time = time.time()

def show_completion(state_records):
    room_completions = 0
    total_rooms = 12
    for completion in state_records:
        #print(completion)
        if state_records[completion]:
            room_completions += 1
        else:
            continue
    completion_percentage = round((room_completions/total_rooms)*100, 1)

    end = time.time()
    print(f"Total runtime of the game is {round((end - start_time), 1)} seconds")

    print(f'You have completed {room_completions} rooms.')
    print(f'You have completed {completion_percentage}% of the game.')

def show_universal_help_text():
    print("- look around        : See what's in the room and what you can do.")
    print("- go <room name>     : Move to another room. Example: go enchanted_library")
    print("- go back            : Return to the previous room")
    print("- ?                  : Show this help message.")
    print("- status             : Show how many rooms you've finished and elapsed time.")
    print("- quit               : Quit the game.")

