from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# Define colours
g = (0, 255, 0)   
b = (0, 0, 255)     
r = (255, 0, 0)   
bg = (0, 0, 0)

direction ="right"

# Labyrinth layout (flattened 8x8 grid)
maze = [
    b, b, b, b, b, b, b, b,
    b, bg, bg, bg, bg, bg, bg, b,
    b, bg, bg, bg, bg, bg, bg, b,
    b, bg, bg, bg, bg, bg, bg, b,
    b, bg, bg, bg, bg, bg, bg, b,
    b, bg, bg, bg, bg, bg, bg, b,
    b, bg, bg, bg, bg, bg, bg, b,
    b, b, b, b, b, b, b, b
]

# Starting position of the player
serpi = [(2, 4), (1, 4), (0, 4)]

def food_spawn():
    while True:
        x, y = random.randint(1, 6), random.randint(1, 6)
        if(x, y) not in serpi:
            return(x, y)
        
food = food_spawn()

def draw():
    sense.clear()
    for segment in serpi:
        sense.set_pixel(segment[0], segment[1], g)
    sense.set_pixel(food[0], food[1], r)

def update_direction():
    global direction
    for event in sense.stick.get_events():
        if event.action != 'pressed':
            continue

        if event.direction == 'up' and direction != "down":
            direction = "up"
        elif event.direction == 'down' and direction != "up":
            direction = "down"
        elif event.direction == 'left' and direction != "right":
            direction = "left"
        elif event.direction == 'right' and direction != "left":
            direction = "right"

def mov_serpi():
    cabeza_x, cabeza_y = serpi[0]
    if direction == "up":
        cabeza_y -= 1
    elif direction == "down":
        cabeza_y += 1
    elif direction == "left":
        cabeza_x -= 1
    elif direction == "right":
        cabeza_x += 1
    nueva_cabeza = (cabeza_x % 7, cabeza_y % 7)
    return nueva_cabeza

while True:
    update_direction()
    nueva_cabeza = mov_serpi()
    
    if nueva_cabeza in serpi:
        sense.show_message("Game Over", text_colour = (255, 0, 0))
        break
    
    serpi.insert(0, nueva_cabeza)
    
    if nueva_cabeza == food:
        food = food_spawn()
    else:
        serpi.pop()
        
    draw()
    sleep(0.2)