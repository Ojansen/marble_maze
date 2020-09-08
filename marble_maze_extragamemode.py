import numpy as np
import pisense as ps
from random import sample
from colorzero import Color
from time import sleep
from signal import signal, SIGTERM
from stopwatch import Stopwatch
stopwatch = Stopwatch()
stopwatch.start()

def sigterm(signum, frame):
    raise SystemExit(0)


def main():
    signal(SIGTERM, sigterm)
    width = height = 8
    colors = {
        'unvisited': Color('black'),
        'visited':   Color('green'),
        'wall':      Color('white'),
        'ball':      Color('red'),
        'goal':      Color('yellow'),
    }
    with ps.SenseHAT() as hat:
        while True:
            maze = generate_maze(width, height, colors)
            inputs = moves(hat.imu)
            outputs = game(maze, colors, inputs)
            display(hat.screen, outputs)
            
            maze1 = generate_maze1(width, height, colors)
            outputs1 = game1(maze1, colors, inputs)
            display(hat.screen, outputs1)



def moves(imu):
    for reading in imu:
        delta_x = int(round(max(-1, min(1, reading.accel.x))))
        delta_y = int(round(max(-1, min(1, reading.accel.y))))
        if delta_x != 0 or delta_y != 0:
            yield delta_y, delta_x
        sleep(1/10)


def display(screen, states):
    try:
        for anim, data in states:
            if anim == 'fade':
                screen.fade_to(data)
            elif anim == 'zoom':
                screen.zoom_to(data)
            elif anim == 'show':
                screen.array = data
            elif anim == 'scroll':
                screen.scroll_text(data, background=Color('red'))
            else:
                assert False
    finally:
        screen.fade_to(ps.array(Color('black')))


def game(maze, colors, moves):
    height, width = maze.shape
    y, x = (1, 1)
    maze[y, x] = colors['ball']
    left, right = clamp(x, width)
    top, bottom = clamp(y, height)
    yield 'fade', maze[top:bottom, left:right]
    for delta_y, delta_x in moves:
        if Color(*maze[y + delta_y, x + delta_x]) != colors['wall']:
            maze[y, x] = colors['visited']
            y += delta_y
            x += delta_x
            if Color(*maze[y, x]) == colors['goal']:
                #yield from game1(maze1, colors, moves)
                break
            else:
                maze[y, x] = colors['ball']
                left, right = clamp(x, width)
                top, bottom = clamp(y, height)
                yield 'show', maze[top:bottom, left:right]
    yield 'fade', ps.array(Color('black'))

def game1(maze1, colors, moves):
    height, width = maze1.shape
    y, x = (1, 1)
    maze1[y, x] = colors['ball']
    left, right = clamp(x, width)
    top, bottom = clamp(y, height)
    yield 'fade', maze1[top:bottom, left:right]
    for delta_y, delta_x in moves:
        if Color(*maze1[y + delta_y, x + delta_x]) != colors['wall']:
            maze1[y, x] = colors['visited']
            y += delta_y
            x += delta_x
            if Color(*maze1[y, x]) == colors['goal']:
                yield from winners_cup()
                break
            else:
                maze1[y, x] = colors['ball']
                left, right = clamp(x, width)
                top, bottom = clamp(y, height)
                yield 'show', maze1[top:bottom, left:right]
    yield 'fade', ps.array(Color('black'))

def generate_maze(width, height, colors):
    walls = generate_walls(width, height)
    maze = ps.array(shape=(2 * height + 1, 2 * width + 1))
    maze[...] = colors['unvisited']
    maze[::2, ::2] = colors['wall']
    for a, b in walls:
        ay, ax = a
        by, bx = b
        y = 2 * by + 1
        x = 2 * bx + 1
        if ay == by:
            maze[y, x - 1] = colors['wall']
        else:
            maze[y - 1, x] = colors['wall']
    maze[0, :] = maze[:, 0] = colors['wall']
    maze[-1, :] = maze[:, -1] = colors['wall']
    maze[-2, -2] = colors['goal']
    return maze

def generate_maze1(width, height, colors):
    walls = generate_walls(width, height)
    maze1 = ps.array(shape=(2 * height + 1, 2 * width + 1))
    maze1[...] = colors['unvisited']
    maze1[::2, ::2] = colors['wall']
    for a, b in walls:
        ay, ax = a
        by, bx = b
        y = 2 * by + 1
        x = 2 * bx + 1
        if ay == by:
            maze1[y, x - 1] = colors['wall']
        else:
            maze1[y - 1, x] = colors['wall']
    maze1[0, :] = maze1[:, 0] = colors['wall']
    maze1[-1, :] = maze1[:, -1] = colors['wall']
    maze1[-2, -2] = colors['goal']
    return maze1


def generate_walls(width, height):
    # Generate the maze with Kruskal's algorithm (there's better
    # choices, but this is a simple demo!)
    sets = {
        frozenset({(y, x)})
        for y in range(height)
        for x in range(width)
    }
    walls = set()
    for y in range(height):
        for x in range(width):
            if x > 0:
                # Add west wall
                walls.add(((y, x - 1), (y, x)))
            if y > 0:
                # Add north wall
                walls.add(((y - 1, x), (y, x)))
    for wall in sample(list(walls), k=len(walls)):
        # For a random wall, find the sets containing the adjacent cells
        a, b = wall
        set_a = set_b = None
        for s in sets:
            if {a, b} <= s:
                set_a = set_b = s
            elif a in s:
                set_a = s
            elif b in s:
                set_b = s
            if set_a is not None and set_b is not None:
                break
        # If the sets aren't the same, the cells aren't reachable;
        # remove the wall between them
        if set_a is not set_b:
            sets.add(set_a | set_b)
            sets.remove(set_a)
            sets.remove(set_b)
            walls.remove(wall)
        if len(sets) == 1:
            break
    assert len(sets) == 1
    assert sets.pop() == {
        (y, x)
        for y in range(height)
        for x in range(width)
    }
    return walls


def clamp(pos, limit, window=8):
    low, high = pos - window // 2, pos + window // 2
    if low < 0:
        high += -low
        low = 0
    elif high > limit:
        low -= high - limit
        high = limit
    return low, high


def winners_cup():
    r = Color('red')
    y = Color('yellow')
    W = Color('white')
    yield 'zoom', ps.array([
        r, r, W, y, y, y, r, r,
        r, r, W, y, y, y, r, r,
        r, r, W, y, y, y, r, r,
        r, r, r, W, y, r, r, r,
        r, r, r, W, y, r, r, r,
        r, r, r, W, y, r, r, r,
        r, r, r, W, y, r, r, r,
        r, r, W, y, y, y, r, r,
    ])
    sleep(2)
    stopwatch.stop()
    score = stopwatch.duration
    score = round(score, 1)
    yield 'fade', ps.array(r)
    yield 'scroll', 'You win!'
    yield 'scroll',(str(score))
    #send score to database


if __name__ == '__main__':
    main()
