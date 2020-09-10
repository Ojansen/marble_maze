from sense_hat import SenseHat
from time import sleep
import time
from lib.constants import maze1, maze2
from lib.send_score import create_post


x = 1
y = 1
sense = SenseHat()
sense.clear()
maze_num = int(1)
selected_maze = None
mazes = [maze1, maze2]
lives = 5


def select_maze():
    global maze_num
    global selected_maze
    maze_num = input("Selecteer een nummer 1 ... 3 or exit with q > ")
    if maze_num == "q":
        sense.clear()
        exit(1)
    else:
        maze_num = int(maze_num)
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
        global lives
        v = (255, 0, 255)
        r = (255, 0, 0)
        if self.maze[new_y][new_x] != r:
            return new_x, new_y
        elif self.maze[new_y][new_x] != r:
            return x, new_y
        elif self.maze[new_y][new_x] != r:
            return new_x, y
        else:
            return x, y

    def check_pit(self, x, y):
        global lives
        global selected_maze
        v = (255, 0, 255)
        if self.maze[x][y] == v:
            sense.set_pixels(sum(selected_maze, []))
            lives -= 1
            print("valkuil")
            main(selected_maze)
        # print(x, y, self.maze[x][y], lives)


if __name__ == "__main__":
    def main(maze):
        physics = MazePhysics(maze=maze)
        game_over = False
        name = None

        b = (0, 0, 0)
        w = (255, 255, 255)
        g = (0, 255, 0)

        x = 1
        y = 1
        while not game_over:
            start_time = time.time()
            o = sense.get_orientation()
            pitch = o["pitch"]
            roll = o["roll"]
            x, y = physics.move_marble(pitch, roll, x, y)
            physics.check_pit(x, y)
            if maze[y][x] == g:
                sense.show_message("win")
                game_over = True
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                name = input("What is you name: ")
                create_post(player_name=name, level=maze_num, tries=lives - 5, score=total_time)
                print('je score is gepost naar http://167.172.37.168/')
                restart()
            elif lives == 0:
                sense.show_message("GAME OVER")
                game_over = True
                restart()
            maze[y][x] = w
            sense.set_pixels(sum(maze, []))
            sleep(0.05)
            maze[y][x] = b

        while game_over:
            pitch = sense.get_orientation()["pitch"]
            roll = sense.get_orientation()["roll"]
            x, y = physics.move_marble(pitch, roll, x, y)
            physics.check_pit(x, y)
            maze[y][x] = w
            sense.set_pixels(sum(maze, []))
            sleep(0.05)
            maze[y][x] = b

    def restart():
        main(maze=select_maze())

    # select_maze()
    restart()
