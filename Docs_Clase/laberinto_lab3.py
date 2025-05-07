from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
# 
# g = (0, 255, 0)
# b = (0, 0, 0)
# r = (255, 0, 0)
# 
# matrix = [
#     g, r, g, g, g, g, g, g,
#     g, b, g ,b ,b ,b ,b, g,
#     g, b, b, b, g, g, b, g,
#     g, g, g, g, g, g, b, g,
#     g, g, b, b, b, g, b, g,
#     g, g, b, g, b, b, b, g,
#     g, g, b, g, g, g, g, g,
#     g, g, b, g, g, g, g, g
#     ]
# 
# sense.set_pixels(matrix)

# ---------------

# message = "si lees esto eres muy guapo/a"
# 
# pause = 0.5
# 
# for letter in message:
#     sense.show_letter(letter)
#     sleep(pause)
# 
# sense.clear()

# ---------------

# def random_colour():
#     return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# 
# g = random_colour()
# 
# matrix = [
#     g, g, g, g, g, g, g, g,
#     g, g, g ,g ,g ,g ,g, g,
#     g, g, g, g, g, g, g, g,
#     g, g, g, g, g, g, g, g,
#     g, g, g, g, g, g, g, g,
#     g, g, g, g, g, g, g, g,
#     g, g, g, g, g, g, g, g,
#     g, g, g, g, g, g, g, g
#     ]
# 
# sense.set_pixels(matrix)

# --------------

# while True:
#     for event in sense.stick.get_events():
#         print(event.direction, event.action)
#         if event.direction == 'up': print(sense.show_letter("U"))
#         elif event.direction == 'down': print(sense.show_letter("D"))
#         elif event.direction == 'left': print(sense.show_letter("L"))
#         elif event.direction == 'right': print(sense.show_letter("R"))
#         else :
#             print(sense.show_letter("M"))
        
# ---------------


        
