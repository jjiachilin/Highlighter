from datetime import datetime
import keyboard
import os
import sys
import re

def record_ts(fh, ls_time):
    time_now = datetime.now()
    delta_time = time_now - ls_time
    print("Timestamp recorded: " + str(delta_time)[:-7])
    fh.write(str(delta_time)[:-7] + "\n")

def main():
    print("Highlighter has started...")
    ls_time = datetime.now()

    while True:
        lecture_start_time = input("Enter the start time of lecture recording(HH:MM:SS): ")
        try:
            ls_time = datetime.strptime(lecture_start_time, '%H:%M:%S')
            break
        except ValueError:
            pass

    print("Press 'ctrl+shift+r' to record the timestamp")
    print("Press 'ctrl+shift+q' to exit program")

    # checks whether the directory exists
    if not os.path.exists('ts_recordings'):
        os.makedirs('ts_recordings')

    # get program start time for file name
    st = datetime.now()
    # correct the year-month-date for ls_time
    ls_time = ls_time.replace(year=st.year, month=st.month, day=st.day)
    formatted_time = ls_time.strftime('%Y-%m-%d_%I-%M-%S%p')

    # get path to write files to ts_recordings directory
    cur_path = os.path.dirname(__file__)
    rel_path = 'ts_recordings\\ts-recording_%s.txt' % formatted_time
    new_path = os.path.join(cur_path, rel_path)

    # open file
    fh = open(new_path, 'w')

    # you may change the keystoke commands as you see fit
    keyboard.add_hotkey('ctrl+shift+r', record_ts, args=[fh, ls_time])
    keyboard.wait('ctrl+shift+q')
    print("Exiting Highlighter...")

    fh.close()


if __name__ == '__main__':
    main()
