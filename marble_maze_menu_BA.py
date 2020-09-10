from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

#sense.show_message("Welcome")
#sleep(3)
sense.show_letter("1")

lvl = 1

#functions
def move_up(event):
    global lvl
    if event.action == "released":
        lvl += 1
    if lvl == 1: 
        sense.show_letter("1")
    if lvl == 2: 
        sense.show_letter("2")
    if lvl == 3: 
        sense.show_letter("3")
    if lvl == 4: 
        sense.show_letter("4")
    if lvl == 5: 
        sense.show_letter("5")
        
def move_down(event):
    global lvl
    if event.action == "released" and lvl > 1:
        lvl -= 1
    if lvl == 1:
        sense.show_letter("1")
    if lvl == 2:
        sense.show_letter("2")
    if lvl == 3:
        sense.show_letter("3")
    if lvl == 4:
        sense.show_letter("4")
    if lvl == 5:
        sense.show_letter("5")

def restart():
        import sys
        #print("argv was",sys.argv)
        #print("sys.executable was", sys.executable)
        print("restart now")
        import os
        os.execv(sys.executable, ['python'] + sys.argv)
        
def move_middle(event):
    game_over = 1
    while game_over == 1:
        if lvl == 1: 
            sense.clear()
            sense.show_message("1")
            game_over = 2
            while game_over == 2:
                    import marble_maze_level_1.py
                    print ("1")
                    execfile('marble_maze_level_1.py')
                    exit(1)
        if lvl == 2: 
            sense.clear()
            sense.show_message("2")
            game_over = 3
            while game_over == 3:
                    import marble_maze_level_2.py
                    print ("2")
                    execfile('marble_maze_level_2.py')
                    exit(1)
        if lvl == 3: 
            sense.clear()
            sense.show_message("3")
            game_over = 4
            while game_over == 4:
                    import marble_maze_level_1_old.py
                    print ("3")
                    execfile('marble_maze_level_1_old.py')
                    restart()
                    
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_middle = move_middle