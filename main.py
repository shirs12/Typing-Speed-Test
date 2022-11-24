import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()  # for not immediately close the program

def wpm_test(stdscr):  # wpd -> word per minute
    target_text = "Hello world this is some test text for this app!"
    current_text = []

    while True:  # checks if the user typed correctly
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:  # colors the text
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        # TODO: TypeError: ord() expected a character, but string of length 8 found
        if ord(key) == 27:  # ASCII representation for 'esc' key
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):  # backspace key representation in the different operating systems
            if len(current_text) > 0:
                current_text.pop()  # remove the last element from the list
        else:
            current_text.append(key)



def main(stdscr):  # std(standard output) screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)
