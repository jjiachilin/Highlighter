from datetime import datetime
import keyboard
import os

def record_ts(fh):
    time_now = datetime.now().time().strftime('%H:%M:%S.%f')
    print("Timestamp recorded: " + str(time_now[:-7]))
    # trim off the microseconds
    fh.write(time_now[:-7] + "\n")

def main():
    print("Highlighter has started...")
    print("Press 'ctrl+shift+r' to record the timestamp")
    print("Press 'ctrl+shift+q' to exit program")

    # checks whether the directory exists
    if not os.path.exists('ts_recordings'):
        os.makedirs('ts_recordings')

    # get program start time for file name
    start_time = datetime.now()
    formatted_time = start_time.strftime('%Y-%m-%d_%I-%M-%S%p')

    # get path to write files to ts_recordings directory
    cur_path = os.path.dirname(__file__)
    rel_path = 'ts_recordings\\ts-recording_%s.txt' % formatted_time
    new_path = os.path.join(cur_path, rel_path)

    fh = open(new_path, 'w')

    # you may change the keystoke commands as you see fit
    keyboard.add_hotkey('ctrl+shift+r', record_ts, args=[fh])
    keyboard.wait('ctrl+shift+q')
    print("Exiting Highlighter...")

    fh.close()


if __name__ == '__main__':
    main()
