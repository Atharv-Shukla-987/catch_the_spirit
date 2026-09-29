import curses
from curses import curs_set, wrapper
import random

current_line = 0
displayed_lines = {}
level = False
my , mx = None , None
scr_y , scr_x = None , None
boundary_warn = False
time = 0
game_start= False
coins = 550
shop_skin = [(100 , [
        " ^",
        "/|\\",
        "/ \\"

    ]), (150 , [
        " _ ",
        "(o)",
        "/|\\",
        "/ \\"
    ]),( 250 , [
        "/\\ /\\",
        "(o_o)",
        "\\|/",
        "/ \\"
    ]) ,
       (300 , [
        " /\\_/\\\\",
        "( O O )",
        " > ^ < ",
        " /   \\ "
    ])
    ]
default_skin = [
        " o",
        "/|\\",
        "/ \\"

    ]

def main(stdscr):
    global level
    global my , mx
    global scr_y , scr_x
    global boundary_warn
    global current_line
    global game_start
    global time
    global coins
    global shop_skin
    global default_skin

    curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK,curses.COLOR_BLACK)
    default_color = curses.color_pair(1)
    transparent_color = curses.color_pair(2)

    scr_y , scr_x = stdscr.getmaxyx()

    gamescr = curses.newwin(scr_y - 2, (scr_x - 2)//2, 2,scr_x//2)
    
    px , py = 10,10
    player = default_skin
    owned = [0]
    mob = [
        "(o o)",
        "|___|"
    ]
    
    def text(i,c):
       global current_line
       global displayed_lines

       i = i[:scr_x - 1]

       if current_line >= scr_y:
              displayed_lines.pop(0,None)
              displayed_lines = {
                     line - 1 : content 
                     for line , content in displayed_lines.items()
              }
              displayed_lines[scr_y -1] = i
              stdscr.clear()

              for line , content in displayed_lines.items():
                     stdscr.addstr(line , 0 , content , transparent_color)

       else:
              displayed_lines[current_line] = i
              stdscr.addstr(current_line,0,i,c)
              if current_line > 0:
               prevs_con = displayed_lines[current_line -1]
               stdscr.addstr(current_line -1 , 0, prevs_con,transparent_color)
              current_line += 1

       stdscr.refresh()

    stdscr.clear()
    text("Press 'p' key to start the game and 'q' to quit", default_color)
    stdscr.refresh()
 
    while True:
        
        time += 1
        py_max , px_max = gamescr.getmaxyx()

        if my is None :
               if mx is None:
                    my = random.randint(3, max(4, py_max - 5))
                    mx = random.randint(3, max(4, px_max - 8))
        
        key = stdscr.getch()

        if px < 2 or py < 2 or px + 2 > px_max - 2 or py + 2 > py_max - 2:
            curses.beep()
            if boundary_warn == False:
                text("you can't go out of the border!", default_color)
                boundary_warn = True

        if key == ord("q"):
            break

        if key == ord("p"):
            game_start = True
            gamescr.clear()
            gamescr.border(
            ord('X'),
            ord('X'),
            ord('o'),
            ord('o'),
            ord('0'),
            ord('0'),
            ord('0'),
            ord('0'),
                )

            for i in range(2000001):
                    if i % 100000 == 0:
                            curses.beep()
                            curses.flash()
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)
                
    
        
        if px == (px_max//5)*3 and py == (py_max//5)*3:
                if level == False:
                        text("do you want to do a mission? (y/n)", default_color)
                        if stdscr.getch() == ord("y"):
                            text("lets go!", default_color)
                            text("level 1 : catch the sprit!", default_color)
                            gamescr.clear()
                            level = True
                            
                                               
                        elif stdscr.getch() == ord("n"):
                            text("nevermind!", default_color)
                        
        elif px == px_max//5 and py == py_max//5:
            if level == False:
                   text(f"You have {coins} coins, wanna buy something? (y/n)", default_color)
                   ans = stdscr.getch()
                   if ans == ord("y"):
                        text("Which skin you wanna buy?",default_color)
                        for i,( price , sprite) in enumerate(shop_skin):
                              status = "OWNED" if i in owned else f"{price} coins"
                              text(f"{i +1}. skin - {status} coins",default_color)
                              for line in sprite:
                                    text(line,default_color)

                        choice = stdscr.getch() - ord("1")

                        if 0 <= choice < len(shop_skin):
                              price, sprite = shop_skin[choice]

                              if choice in owned:
                                    player = sprite
                                    text("Skin equipped!", default_color)
                              elif coins >= price:
                                    coins -= price
                                    owned.append(choice)
                                    player = sprite
                                    text("skin purchased and equipped", default_color)
                              else:
                                    text("Not enough coins!",default_color)
                   elif stdscr.getch() == ord("n"):
                        text("nevermind!", default_color)

        if key == ord("w"):
            if py > 0 :
                py -= 1
            gamescr.clear()
            gamescr.border(
            ord('X'),
            ord('X'),
            ord('o'),
            ord('o'),
            ord('0'),
            ord('0'),
            ord('0'),
            ord('0'),
                )

            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("s"):       
            if py +4 < py_max:
                py += 1
            gamescr.clear()
            gamescr.border(
            ord('X'),
            ord('X'),
            ord('o'),
            ord('o'),
            ord('0'),
            ord('0'),
            ord('0'),
            ord('0'),
                )
            for i, line in enumerate(player):
                             gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("d"):
             if px + 7< px_max:
                px += 1
             gamescr.clear()
             gamescr.border(
             ord('X'),
             ord('X'),
             ord('o'),
             ord('o'),
             ord('0'),
             ord('0'),
             ord('0'),
             ord('0'),
                )

             for i, line in enumerate(player):
                              gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("a"):
             if px > 0:
                px -= 1
             gamescr.clear()
             gamescr.border(
             ord('X'),
             ord('X'),
             ord('o'),
             ord('o'),
             ord('0'),
             ord('0'),
             ord('0'),
             ord('0'),
                )

             for i, line in enumerate(player):
                              gamescr.addstr(py + i , px, line , default_color)

        elif key == ord("m"):
               gamescr.addch((py_max//5)*3, (px_max//5)*3, "M", default_color)
               gamescr.addch(py_max//5, px_max//5, "S", default_color)
        
        if level:
           
            if time%2 == 0:
               moves = [
                     (-1,0),
                     (1,0),
                     (0,-1),
                     (0,1),
                     (-1,-1),
                     (-1,1),
                     (1,-1),
                     (1,1)
               ]
               best_move = None 
               best_distance = -1

               for dy , dx in moves :
                     new_y = my + dy
                     new_x = mx + dx

                     if new_y < 1 or new_y +2> py_max -2:
                           continue
                     if new_x < 1 or new_x +5 > px_max -2:
                           continue

                     dis_sq = (new_x - px)**2 + (new_y - py)**2

                     if dis_sq > best_distance :
                           best_distance = dis_sq
                           best_move = (dy,dx)

               if best_move is not None:
                           my += best_move[0]
                           mx += best_move[1]    

            for i, line in enumerate(mob):
                gamescr.addstr(my + i , mx, line , default_color)
            if (px <= mx <= px +3) and (py <= my<= py +2):
                text("You won the game ! you earned 100 coins ....",default_color)
                coins += 100
                level = False
            
    
            
        
        gamescr.refresh()

if __name__ == "__main__":
    wrapper(main)

