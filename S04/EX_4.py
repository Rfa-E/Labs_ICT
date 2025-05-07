# Deliverables Session 04 - Rafael Antonio Echevarria Silva
# Exercise 4: Use the joystick to show a letter in the
# LED matrix:
# Movement “Up” 🡪 show ‘U’     |   Movement “Down” 🡪 show ‘D’
# Movement “Right” 🡪 show ‘R’  |   Movement “Left” 🡪 show ‘L’
# Movement “Middle” 🡪 show ‘M’

from sense_hat import SenseHat

sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.direction == 'up': print(sense.show_letter("U"))
        elif event.direction == 'down': print(sense.show_letter("D"))
        elif event.direction == 'left': print(sense.show_letter("L"))
        elif event.direction == 'right': print(sense.show_letter("R"))
        else :
            print(sense.show_letter("M"))