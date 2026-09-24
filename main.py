import curses
from curses import wrapper
import time

def main(stdscr):
    gamescr = curses.newwin(35, 175, 2, 2)
    
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
        key = stdscr.getch()
        if key == ord("q"):
            break
        if key == ord("p"):
            game_start = 1
            gamescr.clear()
            gamescr.border(0)

            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)
                
        if game_start == 1:
                stdscr.addstr(0, 0, "Press any key to start the game and 'q' to quit",transparent_color)
        
        
        if key == ord("w"):
            py -= 1
            gamescr.clear()
            gamescr.border(0)
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("s"):       
            py += 1
            gamescr.clear()
            gamescr.border(0)
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("d"):
             px += 1
             gamescr.clear()
             gamescr.border(0)
             for i, line in enumerate(player):
                              gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("a"):
             px -= 1
             gamescr.clear()
             gamescr.border(0)
             for i, line in enumerate(player):
                              gamescr.addstr(py + i , px, line , default_color)

        gamescr.refresh()

if __name__ == "__main__":
    wrapper(main)

