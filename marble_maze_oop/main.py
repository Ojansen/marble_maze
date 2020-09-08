from sense_hat import SenseHat
from time import sleep
from lib.constants import *
from lib.send_score import create_post

sense = SenseHat()
sense.clear()


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
        elif 359 > roll > 181 and y != 0:
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


game_over = False
physics = MazePhysics()
if __name__ == "__main__":
    while not game_over:
        o = sense.get_orientation()
        pitch = o["pitch"]
        roll = o["roll"]
        x, y = physics.move_marble(pitch, roll, x, y)
        if maze[y][x] == g:
            sense.show_message("win")
            game_over = True
            name = input("What is you name: ")
            create_post(player_name=name, level='0', tries='0', score='00:01:30')
            print('je score is gepost naar http://167.172.37.168/highscores')
            exit(1)
        maze[y][x] = w
        sense.set_pixels(sum(maze, []))
        sleep(0.05)
        maze[y][x] = b

    while game_over:
        pitch = sense.get_orientation()["pitch"]
        roll = sense.get_orientation()["roll"]
        x, y = physics.move_marble(pitch, roll, x, y)
        maze[y][x] = w
        sense.set_pixels(sum(maze, []))
        sleep(0.05)
        maze[y][x] = b
