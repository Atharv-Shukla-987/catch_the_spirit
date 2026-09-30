import curses
from curses import curs_set, wrapper
import random
from playsound3 import playsound

current_line = 0
displayed_lines = {}
level = False
my , mx = None , None
scr_y , scr_x = None , None
flicker = False
flicker_time = 0
sound = None
soundlvl = None
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
    global flicker
    global flicker_time
    global soundlvl
    global sound

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
            sound = playsound("bg_song.mp3", block=False )
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

            flicker = True
            flicker_time = 2500
            
            
                          
            
        
        if px == (px_max//5)*3 and py == (py_max//5)*3:
                if level == False:
                        text("do you want to do a mission? (y/n)", default_color)
                        if stdscr.getch() == ord("y"):
                            text("lets go!", default_color)
                            text("level 1 : catch the sprit!", default_color)
                            gamescr.clear()
                            sound.stop()
                            soundlvl = playsound("lvl.mp3",block=False)
                            level = True
                            
                                               
                        elif stdscr.getch() == ord("n"):
                            text("nevermind!", default_color)
                        
        elif px == px_max//5 and py == py_max//5:
            if level == False:
                   text(f"You have {coins} coins, wanna buy something? (y/n)", default_color)
                   ans = stdscr.getch()
                   if ans == ord("y"):
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
                soundlvl.stop()
                sound = playsound("bg_song.mp3",block=False)
                level = False
            
        if flicker:
              laugh = playsound("churail_wali_hasi.mp3",block=False)
              if flicker_time > 0:
                     for i in range( flicker_time):
                        if i % 10 == 0 :
                              curses.flash()
                        flicker_time -=1
              else:
                    flicker = False     
                    laugh.stop()     
                    sound = playsound("bg_song.mp3",block=False)  
                    text("You are invited to halloween party...(enter)",default_color)
                    yes = stdscr.getkey()
                    if yes in ('\n', '\r', 'KEY_ENTER'):
                                 text(" you dont have any costume nor money....(enter)",default_color)
                                 yes1 = stdscr.getkey()
                                 if yes1 in ('\n', '\r', 'KEY_ENTER'):
                                  text("But you have a supernatural ability(enter) ,",default_color)
                                  yes2 = stdscr.getkey()
                                  if yes2 in ('\n', '\r', 'KEY_ENTER'):
                                    text("you can see ghosts and now you have to catch spirts to earn money(enter)",default_color)
                                    yes3 = stdscr.getkey()
                                    if yes3 in ('\n', '\r', 'KEY_ENTER'):
                                      text("for mission and shop you have to go to spirtual points in your world,(enter)",default_color)
                                      yes4 = stdscr.getkey()
                                      if yes4 in ('\n', '\r', 'KEY_ENTER'):
                                        text(" use your ghost vision(press m)(enter)",default_color)
                                        yes = stdscr.getkey()
                                        if yes in ('\n', '\r', 'KEY_ENTER'):
                                              text("Use WASD to move",default_color)
        
        gamescr.refresh()

if __name__ == "__main__":
    wrapper(main)

