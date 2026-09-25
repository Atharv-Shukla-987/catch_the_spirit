import curses
from curses import curs_set, wrapper





def main(stdscr):
    
    curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK,curses.COLOR_BLACK)
    default_color = curses.color_pair(1)
    transparent_color = curses.color_pair(2)

    
    px , py = 10,10
    player = [
        " o",
        "/|\\",
        "/ \\"

    ]

    def text(i,c):
       current_line = 0
       stdscr.addstr(current_line , 0,i,c)
       current_line += 1
       
              

    stdscr.clear()
    text("Press 'p' key to start the game and 'q' to quit",default_color)
    stdscr.refresh()
    while True:
        scr_y , scr_x = stdscr.getmaxyx()
        gamescr = curses.newwin(scr_y - 2, (scr_x - 2)//2, 2,scr_x//2)
        py_max , px_max = gamescr.getmaxyx()
        key = stdscr.getch()

        
        if px < 3 or py < 3 or px + 3 > px_max - 3 or py + 3 > py_max - 3:
                curses.beep()

        if key == ord("q"):
            break

        if key == ord("p"):
            game_start = True
            gamescr.clear()
            gamescr.border(0)
            
            for i in range(2000001):
                    if i % 100000 == 0:
                            curses.beep()
                            curses.flash()
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)
                
    
        
        if px == px_max//4 and py == py_max//4:
                text("do you want to do a mission? (y/n)", default_color)
                if stdscr.getch() == ord("y"):
                        text("lets go!", default_color)
                        text("do you want to do a mission? (y/n)", transparent_color)
                elif stdscr.getch() == ord("n"):
                        text("nevermind!", default_color)
                        text("do you want to do a mission? (y/n)", transparent_color)
        elif px == px_max//5 and py == py_max//5:
            text("do you want to shop? (y/n)", default_color)
            if stdscr.getch() == ord("y"):
                text("lets go!", default_color)
                text("do you want to shop? (y/n)", transparent_color)
            elif stdscr.getch() == ord("n"):
                text("nevermind!", default_color)
                text("do you want to shop? (y/n)", transparent_color)

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

        gamescr.addch(py_max//4, px_max//4, "M", default_color)
        gamescr.addch(py_max//5, px_max//5, "S", default_color)

        gamescr.refresh()

if __name__ == "__main__":
    wrapper(main)

