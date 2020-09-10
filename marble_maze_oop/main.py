from sense_hat import SenseHat
from time import sleep
from lib.constants import maze1, maze2
from lib.send_score import create_post


r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,255,0)
v = (30,80,30)

x = 1
y = 1
sense = SenseHat()
sense.clear()
maze_num = int(1)
selected_maze = None
mazes = [maze1, maze2]
lives = 3


def select_maze():
    global maze_num
    global selected_maze
    maze_num = int(input("Selecteer een nummer 1, 2, 3 > "))
    selected_maze = mazes[maze_num - 1]
    return mazes[maze_num - 1]


class MazePhysics:
    def __init__(self, maze=selected_maze):
        self.maze = maze

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
        if self.maze[new_y][new_x] != r:
            return new_x, new_y
        elif self.maze[new_y][new_x] != r:
            return x, new_y
        elif self.maze[new_y][new_x] != r:
            return new_x, y
        else:
            return x, y

    def check_pit(self, new_x, new_y):
        global lives
        if self.maze[new_y][new_x] == v:
            lives -= 1
            print(lives)


if __name__ == "__main__":
    def main(maze):
        physics = MazePhysics(maze=maze)
        game_over = False
        r = (255, 0, 0)
        b = (0, 0, 0)
        w = (255, 255, 255)
        g = (0, 255, 0)

        x = 1
        y = 1
        name = None
        while not game_over:
            o = sense.get_orientation()
            pitch = o["pitch"]
            roll = o["roll"]
            x, y = physics.move_marble(pitch, roll, x, y)
            physics.check_pit(x, y)
            if maze[y][x] == g or lives == 0:
                sense.show_message("win")
                game_over = True
                name = input("What is you name: ")
                create_post(player_name=name, level='str(maze)', tries=lives, score='00:01:30')
                print('je score is gepost naar http://167.172.37.168/highscores')
                restart()
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

    def restart():
        game = main(maze=select_maze())

    # select_maze()
    restart()
