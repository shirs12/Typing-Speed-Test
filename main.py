import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()  # for not immediately close the program

def display_text(stdscr, target, current, wpm=0):  # wpm is an optional parameter with a default value of 0
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):  # getting the char as well as the index
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)  # colors each char of the text

def load_text():
    # open text.txt file in read mode, and stores it in 'f'. 'with' make sure the file will be close after it opens.
    with open("text.txt", "r") as f:
        lines = f.readlines()  # accessing the file using 'f'
        return random.choice(lines).strip()  # returns a random line from the file

def wpm_test(stdscr):  # wpd -> word per minute
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  # lets the wpm keep running

    while True:  # checks if the user typed correctly
        time_elapsed = max(time.time() - start_time, 1)  # max function for not get division by 0 error

        # calculates the characters per minute divided by 5,
        # which is the average word length, to get words per minute
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # "".join -> combines all the characters to a string with an empty string seperator
        if "".join(current_text) == target_text:  # checks if the user done writing the target text correctly
            stdscr.nodelay(False)  # wait for the user to hit a key without getting an error
            break

        # make sure the program won't crash in case the user doesn't type something
        try:
            key = stdscr.getkey()
        except:
            continue  # skip to the next round of the loop

        if ord(key) == 27:  # ASCII representation for 'esc' key
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):  # backspace key representation in the different operating systems
            if len(current_text) > 0:
                current_text.pop()  # remove the last element from the list
        elif len(current_text) < len(target_text):  # make sure we cannot add more text than the target text
            current_text.append(key)



def main(stdscr):  # std(standard output) scr(screen)
    # text colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        # asks the user if he wants to play again
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue or esc to exit... ")
        key = stdscr.getkey()  # waits for the user to type a key
        if ord(key) == 27:  # the game will continue, unless the user presses the esc key to exit
            break



wrapper(main)
