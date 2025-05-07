from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

# Apartado a
# a.1

red = (255, 0, 0)
green = (0, 255, 0)

sense.show_letter("J")

# a.2
while True:
    
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    
    message =  "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
    
    print(message)
    print("\n")
    
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)
    
    print("Acceleration on each axis: x={0}, y={1}, z={2}".format(x, y, z))
    print("--------------------------------------------------------------")
    
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)
    
    time.sleep(1)
    