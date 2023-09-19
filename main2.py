import curses

def window_setup(window):
    curses.curs_set(0)
    window.timeout(-1)
    window.keypad(1)
    window.border(0)

def main(window):
    window_setup(window)
    
    h, w = window.getmaxyx()  # Get the maximum height and width of the window

    y, x = h//2, w//2  # Set the initial position of the player to the center

    window.addch(y, x, '#')
    window.refresh()

    while True:
        key = window.getch()

        if key == ord('q'):
            break

        if key == -1:
            continue

        if key == curses.KEY_DOWN and y < h - 3:
            y += 1
        if key == curses.KEY_UP and y > 1:
            y -= 1
        if key == curses.KEY_LEFT and x > 1:
            x -= 1
        if key == curses.KEY_RIGHT and x < w - 2:
            x += 1

        window.clear()
        window.border(0)
        window.addch(y, x, '#')
        window.addstr(h - 2, 1, "Arrows: Move  q: Quit")  # Add instruction text at the bottom

        window.refresh()

curses.wrapper(main)
