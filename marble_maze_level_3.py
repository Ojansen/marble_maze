from sense_hat import SenseHat
from time import sleep
import time
from datetime import datetime
from stopwatch import Stopwatch
# from constants import *
from mazes import *

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
stopwatch = Stopwatch()

sense = SenseHat()
sense.clear()

stopwatch.restart()

maze = maze1


class MazePhysics:
    def move_marble(self, pitch, roll, x, y):
        new_x = x
        new_y = y
        if 1 < pitch < 179 and x != 0:
            new_x -= 1
        elif 359 > pitch > 181 and x != 7:
            new_x += 1
        if 1 < roll < 179 and y != 7:
            new_y += 1
        elif 359 >r oll > 181 and y != 0:
            new_y -= 1
        new_x, new_y = self.check_wall(x, y, new_x, new_y)
        return new_x, new_y

    def check_wall(self, x, y, new_x, new_y):
        if maze[new_y][new_x] != r:
            return new_x, new_y
        elif maze[new_y][new_x] != r:
            return x, new_y
        elif maze[new_y][new_x] != r:
            return new_x, y
        else:
            return x, y


class Engine:
    game_running = True

    def __init__(self):
        pass

    def play(self):
        while self.game_running:
            pitch = sense.get_orientation()["pitch"]
            roll = sense.get_orientation()["roll"]
            x, y = game.move_marble(pitch, roll)
            maze[y][x] = w
            sense.set_pixels(sum(maze, []))
            sleep(0.05)
            maze[y][x] = b

    def game_over(self):
        if not self.game_running:
            o = sense.get_orientation()
            pitch = o["pitch"]
            roll = o["roll"]
            x, y = game.move_marble(pitch, roll)


game = MazePhysics(x=1, y=1)
engine = Engine()
engine.play()

while not game_over:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x, y = game.move_marble(pitch, roll)
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
        x = 6
        y = 1
        sense.clear()
    if maze[y][x] == t9:
        maze = maze1
        x = 3
        y = 6
        sense.clear()
    if maze[y][x] == t10:
        maze = maze1
        x = 6
        y = 6
        sense.clear()
    if maze[y][x] == t11:
        maze = maze4
        x = 1
        y = 4
        sense.clear()
    if maze[y][x] == t12:
        maze = maze2
        x = 1
        y = 6
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
        stopwatch.stop()
        score = stopwatch.duration
        score = round(score, 1)
        sense.show_message("score")
        sense.show_message(str(score))
        #send score to database
        #exit()
        game_over = True
    maze[y][x] = w
    sense.set_pixels(sum(maze, []))
    sleep(0.05)
    maze[y][x] = b



