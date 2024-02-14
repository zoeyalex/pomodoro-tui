#!/usr/bin/python
from config import task_duration, short_break_duration, long_break_duration
import time


def get_integer_input(prompt="Session length in pomodoros: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please ensure integer input\n")

# for debugging
def generate_pomodoro_schedule(session_length, task_duration, short_break_duration, long_break_duration):
    pomodoro_count = 0
    schedule = []
    data = {
            "n_task": 0,
            "n_short_break": 0,
            "n_long_break": 0,
    }
    for _ in range(session_length):
        # check for long break
        if pomodoro_count == 3:
            schedule.append(task_duration)
            schedule.append(long_break_duration)
            pomodoro_count = 0
            continue
        schedule.append(task_duration)
        schedule.append(short_break_duration)
        pomodoro_count += 1
    return schedule

def timer(duration):
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time < duration:
        elapsed_time = time.time() - start_time
        print(f"\rElapsed Time: {round(elapsed_time)} seconds", end="", flush=True)
        time.sleep(1)  # Sleep for 1 second
    print("\rTimer finished!")



if __name__ == "__main__":
    session_length = get_integer_input()
    schedule = generate_pomodoro_schedule(session_length, task_duration, short_break_duration, long_break_duration)
    print(schedule)
    for ele in schedule:
        timer(ele)
