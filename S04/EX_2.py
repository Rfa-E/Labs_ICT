# Deliverables Session 04 - Rafael Antonio Echevarria Silva
# Exercise 2: Could we display a message using “show_letter” function?
## We can solve it introducing a pause between letters

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

message = "Exercise 2: Rafael Echevarria Silva"

pause = 0.5

for letter in message:
    sense.show_letter(letter, text_colour=[255, 0, 0], back_colour=[0, 0, 125])
    sleep(pause)

sense.clear()