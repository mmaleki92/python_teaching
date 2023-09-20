import datetime
import time
import winsound

def set_alarm():
    """
    Prompts the user to input the desired alarm time and returns it as a datetime object.
    """
    print("Enter alarm time in 24-hour format (HH:MM)")
    while True:
        try:
            time_str = input("> ")
            alarm_time = datetime.datetime.strptime(time_str, "%H:%M")
            return alarm_time
        except ValueError:
            print("Invalid time format! Please enter time in HH:MM format.")

def play_alarm():
    """
    Plays an alarm sound repeatedly until the user stops it by pressing any key.
    """
    frequency = 1000
    duration = 1000
    while True:
        winsound.Beep(frequency, duration)
        time.sleep(0.5)
        if msvcrt.kbhit():
            break

alarm_time = set_alarm()
print(f"Alarm set for {alarm_time.strftime('%H:%M')}")

while True:
    current_time = datetime.datetime.now().time()
    if current_time >= alarm_time.time():
        print("Time's up!")
        play_alarm()
        break
    time.sleep(1)

