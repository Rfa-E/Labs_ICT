# Deliverables Session 04 - Rafael Antonio Echevarria Silva
# a) Draw a labyrinth (For example something similiar like that)

from sense_hat import SenseHat

sense = SenseHat()

g = (0, 255, 0)
b = (0, 0, 0)
r = (255, 0, 0)

matrix = [
    g, r, g, g, g, g, g, g,
    g, b, g ,b ,b ,b ,b, g,
    g, b, b, b, g, g, b, g,
    g, g, g, g, g, g, b, g,
    g, g, b, b, b, g, b, g,
    g, g, b, g, b, b, b, g,
    g, g, b, g, g, g, g, g,
    g, g, b, g, g, g, g, g
    ]

sense.set_pixels(matrix)