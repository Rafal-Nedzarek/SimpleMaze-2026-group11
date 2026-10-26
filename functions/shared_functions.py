import time
from operator import itemgetter

start_time = time.time()
previous_duration= 0

def show_completion(state_records,state):
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
    duration=end - start_time + previous_duration
    print(f"Current runtime of the game is {convert(duration)}")
    print(f"Total runtime of the game is {convert(state["total_playtime"] + duration)}")
    print(f'You have completed {room_completions} rooms.')
    print(f'You have completed {completion_percentage}% of the game.')
    print(f"\nYour current health is {state['health']}/10 hearts.")
    print("- Your current inventory:", state["inventory"])
    return duration

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def show_universal_help_text():
    print("- look around        : See what's in the room and what you can do.")
    print("- go <room name>     : Move to another room. Example: go enchanted_library")
    print("- go back            : Return to the previous room")
    print("- ?                  : Show this help message.")
    print("- status             : Show how many rooms you've finished and elapsed time.")
    print("- quit               : Quit the game.")

def healing(state):
    state["health"] += 4
    if state["health"] > 10:
        state["health"] = 10
    state["inventory"].remove("bandages")
    print("You used the bandages.")
    print(f"\n- Your current health is {state["health"]} hearts")
    print("- Your current inventory:", state["inventory"])

def write_save_file(username, states):
    from pathlib import Path

    path = Path("functions/save_files/" + username + "_save.txt")

    end = time.time()
    duration = end - start_time + previous_duration
    states["total_playtime"] += duration

    lines = [str(states)]

    with path.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)

def read_save_file(username):

    global start_time
    start_time = time.time()

    from pathlib import Path

    path = Path("functions/save_files/" + username + "_save.txt")

    if Path.is_file(path):
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                getDict = dict(eval(line))
                return getDict

    else:
        return None

def write_to_leaderboard(states):
    room_completions = 0
    total_rooms = 12
    for completion in states['completed'].values():
        if completion:
            room_completions += 1
        else:
            continue
    completion_percentage = round((room_completions / total_rooms) * 100, 1)

    end = time.time()
    duration = end - start_time + previous_duration
    completion_time = states["total_playtime"] + duration

    from pathlib import Path

    path = Path("functions/save_files/leaderboard.txt")

    completion_data = {"username" : states["user_name"], "completion_percent": completion_percentage,
                                  "total_playtime": completion_time}

    lines = [str(completion_data)]

    with path.open("a", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def display_leaderboard():

    completion_list = []

    from pathlib import Path

    path = Path("functions/save_files/leaderboard.txt")

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line == "":
                pass
            else:
                completion_list.append( dict(eval(line)) )
                pass

    print("Sorted by completion percent: ",
          sorted(completion_list, key=itemgetter('completion_percent'), reverse=True))
    print("Sorted by play time: ",
          sorted(completion_list, key=itemgetter('total_playtime')))
