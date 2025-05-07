# Deliverables Session 04 - Rafael Antonio Echevarria Silva
# Exercise 3: We can select a colour but, ¿is it possible to select a random colour?
# ## We can solve it using the function random_colour() to select a random colour

from sense_hat import SenseHat
import random

sense = SenseHat()

def random_colour():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

g = random_colour()

matrix = [
    g, g, g, g, g, g, g, g,
    g, g, g ,g ,g ,g ,g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
    ]

sense.set_pixels(matrix)