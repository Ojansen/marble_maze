from sense_hat import SenseHat
from time import sleep
import time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

sense = SenseHat()
sense.clear()

r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,255,0)
t1 = (0,1,0)
t2 = (0,2,0)
t3 = (0,3,0)
t4 = (0,4,0)
t5 = (0,5,0)
t6 = (0,6,0)
t7 = (0,7,0)
t8 = (0,8,0)
t9 = (0,9,0)
t10 = (0,10,0)
t11 = (0,11,0)
t12 = (0,12,0)
t13 = (0,13,0)
t14 = (0,14,0)

x = 1
y = 1

maze1 = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,t1],
        [r,b,r,b,r,r,r,r],
        [r,b,r,b,b,b,b,r],
        [r,b,r,r,r,b,b,r],
        [r,b,b,b,r,b,b,t2],
        [r,b,r,b,r,r,b,r],
        [r,r,r,t3,r,r,t4,r]]

maze2 = [[r,r,r,r,r,r,r,r],
        [t5,b,b,b,b,r,b,r],
        [r,b,r,r,b,r,b,r],
        [r,b,b,r,b,r,b,r],
        [r,r,r,r,b,b,b,r],
        [t6,b,b,b,b,r,b,r],
        [r,b,b,b,b,r,b,r],
        [r,t7,r,r,r,r,t8,r]]

maze3 = [[r,r,r,t9,r,r,t10,r],
         [r,b,b,b,r,r,b,r],
         [r,b,r,r,b,r,b,r],
         [r,b,r,r,b,r,r,r],
         [r,b,r,r,b,b,b,t11],
         [r,b,g,r,b,r,b,r],
         [r,b,r,r,b,r,b,r],
         [r,r,r,r,r,r,r,r]]

maze4 = [[r,t12,r,r,r,r,t13,r],
         [r,b,r,b,b,r,b,r],
         [r,b,b,r,b,r,b,r],
         [r,r,r,r,b,b,r,r],
         [t14,b,b,r,b,b,b,r],
         [r,b,r,r,r,r,b,r],
         [r,b,b,b,b,b,b,r],
         [r,r,r,r,r,r,r,r]]

maze = maze1

game_over = False

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 20 <pitch < 179 and x != 0:
        new_x -= 1
    elif 340 >pitch > 181 and x != 7:
        new_x += 1
    if 20 <roll < 179 and y != 7:
        new_y += 1
    elif 340 >roll > 181 and y != 0:
        new_y -= 1
    new_x, new_y = check_wall(x,y,new_x,new_y)
    return new_x, new_y
    
def check_wall(x,y,new_x,new_y):
    if maze[new_y][new_x] !=r:
        return new_x, new_y
    elif maze[new_y][new_x] !=r:
        return x, new_y
    elif maze[new_y][new_x] !=r:
        return new_x, y
    else:
        return x,y
while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch,roll,x,y)
    if maze[y][x] == t1:
        maze = maze2
        x = 1
        y = 1
    if maze[y][x] == t2:
        maze = maze2
        x = 1
        y = 5
    if maze[y][x] == t3:
        maze = maze3
        x = 3
        y = 1
        sense.clear()
    if maze[y][x] == t4:
        maze = maze3
        x = 6
        y = 1
        sense.clear()
    if maze[y][x] == t5:
        maze = maze1
        x = 6
        y = 1
        sense.clear()
    if maze[y][x] == t6:
        maze = maze1
        x = 6
        y = 5
        sense.clear()
    if maze[y][x] == t7:
        maze = maze4
        x = 1
        y = 1
        sense.clear()
    if maze[y][x] == t8:
        maze = maze4
        x = 1
        y = 6
        sense.clear()
    if maze[y][x] == t9:
        maze = maze1
        x = 6
        y = 3
        sense.clear()
    if maze[y][x] == t10:
        maze = maze1
        x = 6
        y = 6
        sense.clear()
    if maze[y][x] == t11:
        maze = maze4
        x = 4
        y = 1
        sense.clear()
    if maze[y][x] == t12:
        maze = maze2
        x = 6
        y = 1
        sense.clear()
    if maze[y][x] == t13:
        maze = maze2
        x = 6
        y = 6
        sense.clear()
    if maze[y][x] == t14:
        maze = maze3
        x = 6
        y = 4
        sense.clear()
    if maze[y][x] == g:
        sense.show_message("win")
        #sense.show_message
        #timer en highscore systeem
        #exit script
        game_over = True
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b
while not game_over:
    pitch = sense.get_orientation()["pitch"]
    roll = sense.get_orientation()["roll"]
    x,y = move_marble(pitch,roll,x,y)
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b
    
