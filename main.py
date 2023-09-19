import curses

def window_setup(window):
    curses.curs_set(0)
    window.timeout(-1)  # Change this line to wait indefinitely for the player's input
    window.keypad(1)
    h, w = window.getmaxyx()
    window.border(0)

def create_snake(window, w, h):
    snake_x = w//2
    snake_y = h//2
    snake_body = [
        [snake_y, snake_x],
        [snake_y, snake_x-1],
        [snake_y, snake_x-2],
        [snake_y, snake_x-3]
    ]
    return snake_body

def main(window):
    window_setup(window)
    h, w = window.getmaxyx()
    w = w//2
    key = -1

    snake_body = create_snake(window, w, h)

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        if key == -1:
            continue

        new_head = [snake_body[0][0], snake_body[0][1]]

        if key == curses.KEY_DOWN and new_head[0] < h - 2:
            new_head[0] += 1
        if key == curses.KEY_UP and new_head[0] > 1:
            new_head[0] -= 1
        if key == curses.KEY_LEFT and new_head[1] > 1:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT and new_head[1] < w - 2:
            new_head[1] += 1

        if new_head in snake_body[1:]:
            continue

        snake_body.insert(0, new_head)
        snake_body.pop()

        window.clear()
        window.border(0)
        for y, x in snake_body:
            window.addch(y, x, '#')

        window.refresh()

curses.wrapper(main)
