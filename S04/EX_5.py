from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

g = (0, 255, 0)   # Wall
b = (0, 0, 0)     # Path
r = (255, 0, 0)   # Player

maze = [
    g, b, g, g, g, g, g, g,
    g, b, g, b, b, b, b, g,
    g, b, b, b, g, g, b, g,
    g, g, g, g, g, g, b, g,
    g, g, b, b, b, g, b, g,
    g, g, b, g, b, b, b, g,
    g, g, b, g, g, g, g, g,
    g, g, b, g, g, g, g, g
]

player_x = 1
player_y = 0

def maze_at(x, y):
    return maze[y * 8 + x]

def draw_maze():
    display = maze[:]
    display[player_y * 8 + player_x] = r
    sense.set_pixels(display)

draw_maze()

while True:
    for event in sense.stick.get_events():
        if event.action != 'pressed':
            continue

        new_x, new_y = player_x, player_y

        if event.direction == 'up':
            new_y = max(0, player_y - 1)
        elif event.direction == 'down':
            new_y = min(7, player_y + 1)
        elif event.direction == 'left':
            new_x = max(0, player_x - 1)
        elif event.direction == 'right':
            new_x = min(7, player_x + 1)

        if maze_at(new_x, new_y) == b:
            player_x, player_y = new_x, new_y
            draw_maze()