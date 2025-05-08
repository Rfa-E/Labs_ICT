from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

g = (0, 255, 0)   # Color de la serpiente
r = (255, 0, 0)   # Color de la comida

direction = "right"
serpi = [(2, 4), (1, 4), (0, 4)]
contador = 0

def food_spawn():
    while True:
        x, y = random.randint(1, 6), random.randint(1, 6)
        if (x, y) not in serpi:
            return (x, y)

food = food_spawn()

def draw():
    sense.clear()
    for segment in serpi:
        sense.set_pixel(segment[0], segment[1], g)
    sense.set_pixel(food[0], food[1], r)

def update_direction():
    global direction
    accel = sense.get_accelerometer_raw()
    x = accel['x']
    y = accel['y']

    if abs(x) > abs(y): 
        if x > 0.2 and direction != "left":
            direction = "right"
        elif x < -0.2 and direction != "right":
            direction = "left"
    else: 
        if y > 0.2 and direction != "up":
            direction = "down"
        elif y < -0.2 and direction != "down":
            direction = "up"

def dead(muerte):
    if muerte:
        sense.show_message(f"Game Over Puntos: {contador}", text_colour=(255, 0, 0))
        sleep(2)
        exit()

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
    if not (0 <= cabeza_x < 8 and 0 <= cabeza_y < 8):
        dead(True)
    return cabeza_x, cabeza_y

while True:
    update_direction()
    nueva_cabeza = mov_serpi()

    if nueva_cabeza in serpi:
        dead(True)

    serpi.insert(0, nueva_cabeza)

    if nueva_cabeza == food:
        food = food_spawn()
        contador += 1
    else:
        serpi.pop()

    draw()
    sleep(0.6)
