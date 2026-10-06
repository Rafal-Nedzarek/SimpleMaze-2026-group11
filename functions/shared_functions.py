def show_completion(state_records):
    room_completions = 0
    total_rooms = 12
    for completion in state_records:
        print(completion)
        if state_records[completion]:
            room_completions += 1
        else:
            continue
    completion_percentage = round((room_completions/total_rooms)*100, 1)
    print(f'You have completed {room_completions} rooms.')
    print(f'You have completed {completion_percentage}% of the game.')

def show_universal_help_text():
    pass

