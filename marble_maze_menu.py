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

def move_middle(event):
    sense.clear()
    
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_middle = move_middle