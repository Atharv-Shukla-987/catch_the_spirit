import curses
from curses import curs_set, wrapper


def main(stdscr):
    
    curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK,curses.COLOR_BLACK)
    default_color = curses.color_pair(1)
    transparent_color = curses.color_pair(2)
    
    px , py = 2,2
    player = [
        " o",
        "/|\\",
        "/ \\"

    ]


    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'p' key to start the game and 'q' to quit",default_color)
    stdscr.refresh()
    while True:
        scr_y , scr_x = stdscr.getmaxyx()
        gamescr = curses.newwin(scr_y - 2, scr_x - 2, 2, 2)
        py_max , px_max = gamescr.getmaxyx()
        key = stdscr.getch()
        if key == ord("q"):
            break
        if key == ord("p"):
            game_start = 1
            gamescr.clear()
            gamescr.border(0)
            for i in range(2000001):
                    if i % 100000 == 0:
                            curses.beep()
                            curses.flash()
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)
                
        if game_start == 1:
                stdscr.addstr(0, 0, "Press any key to start the game and 'q' to quit",transparent_color)
        
        
        if key == ord("w"):
            if py > 0 :
                py -= 1
            gamescr.clear()
            gamescr.border(0)
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("s"):       
            if py +3 < py_max:
                py += 1
            gamescr.clear()
            gamescr.border(0)
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("d"):
             if px + 4< px_max:
                px += 1
             gamescr.clear()
             gamescr.border(0)
             for i, line in enumerate(player):
                              gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("a"):
             if px > 0:
                px -= 1
             gamescr.clear()
             gamescr.border(0)
             for i, line in enumerate(player):
                              gamescr.addstr(py + i , px, line , default_color)

        gamescr.refresh()

if __name__ == "__main__":
    wrapper(main)

