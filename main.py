import curses
from curses import wrapper
import time

# 30:30
# type in file directory 'cmd' and then type 'python main.py' and the code will run

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


def wpm_test(stdscr):  # wpd -> word per minute
    target_text = "Hello world this is some test text for this app!"
    current_text = []
    wpm = 0
    start_time = time.time()

    while True:  # checks if the user typed correctly
        time_elapsed = max(time.time() - start_time, 1)  # max function for not get division by 0 error

        # calculates the characters per minute divided by 5,
        # which is the average word length, to get words per minute
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        key = stdscr.getkey()

        # TODO: TypeError: ord() expected a character, but string of length 8 found
        if ord(key) == 27:  # ASCII representation for 'esc' key
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):  # backspace key representation in the different operating systems
            if len(current_text) > 0:
                current_text.pop()  # remove the last element from the list
        elif len(current_text) < len(target_text):  # make sure we cannot add more text than the target text
            current_text.append(key)



def main(stdscr):  # std(standard output) screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)
