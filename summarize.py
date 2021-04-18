import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Error: please specify a transcript file in the command line argument")
        return
    elif len(sys.argv) > 2:
        print("Error: please specify only one transcript file")
        return

    # reads in the relative path to the file
    cur_path = os.path.dirname(__file__)
    new_path = os.path.join(cur_path, sys.argv[1])

    try:
        fh = open(new_path, 'r')
    except IOError:
        print("Error opening the specified to read")

    ts_list = fh.readlines()
    # maps the absolute timestamp to the transcript time stamp
    # don't know how to do that yet
    # for ts in ts_list:
    # use ts.strip() to remove the new line char

    # after getting the texts from the transcript time stamp
    # send them into OpenAI to summarize

    # output to a text file of the summary

    fh.close()
    


if __name__ == '__main__':
    main()